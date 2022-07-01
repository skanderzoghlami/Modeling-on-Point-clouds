# -*- coding: utf-8 -*-
"""PC_To_Graph.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xlk_hX-P63HZ25GCp8x1G83a-bX3bf-f

## Packages download :
"""

!pip install open3d scipy spektral

"""## Libraries and Loading the point clouds :"""

import open3d as o3d
import tensorflow as tf
import numpy as np
import spektral
from tensorflow.keras.layers import Dropout, Input
from tensorflow import keras
from tensorflow.keras import layers
from scipy import sparse
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Dropout
from spektral.layers import GCNConv, GlobalSumPool
from spektral.data import BatchLoader
from spektral.data.loaders import Loader
from spektral.layers import ChebConv
from spektral.data import Dataset
from scipy.spatial import distance_matrix
from spektral.data import Graph
import os
import glob
from scipy.sparse import save_npz
from spektral.layers import GATConv

path ="/content/data/clean_train/predlift/boxer/original.ply"

pcd = o3d.io.read_point_cloud("/content/data/clean_train/predlift/8boxer/original.ply")
pcd

pcd_xyz = np.asarray(pcd.points)
pcd_rgb = np.asarray(pcd.colors)
full_pc = np.concatenate((pcd_xyz,pcd_rgb),axis=1)

def distance(xi,xj):
  return np.exp(-1* np.linalg.norm(xi-xj))
# Adjacency Matrix
def pc_to_adj(pcd):
  A=[]
  for i in pcd.points:
    row=[]
    for j in pcd.points:
      row.append(distance(i,j))
    A.append(row)
  return A

original_pcd = o3d.io.read_point_cloud(path)
A= distance_matrix(original_pcd.points[0:2048],original_pcd.points[0:2048])
from scipy import sparse
sA = sparse.csr_matrix(A)
print(sA)

# Degree Matrix
def adj_to_d(A):
  D=np.zeros([2048,2048])
  s=np.sum(np.asarray(A),axis=0)
  for i in range(0,2048):
    D[i][i]=np.sum(s[i])
  return D

# Degree Matrix
# D= adj_to_d(A)

# Graph laplacian 
#Lc = D - A

"""## Transforming the graph Signal from RGB to YUV :"""

def rgb_to_yuv(rgb):
    y= 0.299 * rgb[0] + 0.587*rgb[1]+ 0.114 * rgb[2]
    u = 0.492 * (rgb[2]-y)
    v=0.877* (rgb[0]-y)
    return [y, u ,v]

yuv_colors=[]
rgb_colors=pcd.colors
for rgb in rgb_colors:
    yuv_colors.append(rgb_to_yuv(rgb))

# Graph Signals : 
Hy = np.array(yuv_colors)[:,0]
Hu = np.array(yuv_colors)[:,1]
Hv = np.array(yuv_colors)[:,2]

"""## Importing Data :  """

from google.colab import drive
drive.mount('/content/gdrive')

!unrar x -Y "/content/gdrive/MyDrive/SKANDER/train_data.rar" "/content/data"

def corrector(s):
    for a in range(0,len(s)):
        if (s[a]=='\''):
            s[a]='/'
    return s

"""## Loss function :"""

def custom_loss_function(y_true, y_pred):
  squared_difference = tf.square(y_true - y_pred)
  return tf.reduce_mean(squared_difference, axis=-1)

"""## Graphs generation from point clouds : """

!rm -r /content/spektral/datasets/PatchDatasets
#!mkdir spektral spektral/datasets
dataset=[]

class PatchDatasets(Dataset):
    """
    A dataset for the graphs
    """
    def read(self):
      output = []
      iter = 0
      for name in glob.glob('/content/spektral/datasets/PatchDatasets/*.npz'):
        data = np.load(name,allow_pickle=True)
        output.append(
            Graph(x=data['x'], a=data['a'], y=data['y'])
        )
        iter+=1
        if(iter == 50):
          return output
      return output
    def download(self):
        # Create the directory
        if os.path.exists("/content/spektral/datasets/PatchDatasets/"):
          return 
        os.mkdir('/content/spektral/datasets/PatchDatasets/')
        for name in glob.glob('/content/data/clean_train/predlift/boxer/r01.ply'):
            pcd = o3d.io.read_point_cloud(corrector(name))
            pcdy = o3d.io.read_point_cloud("/content/data/clean_train/predlift/"+name.split('/')[-2]+"/original.ply")
            i=0
            # Patch creation
            while(i<=len(pcd.points)/2048):
                nd = []
                rgb= []
                rgby=[]
                if(i==len(pcd.points)/2048):
                    nd = pcd.points[i*2048:]
                    rgb= pcd.colors[i*2048:]
                    rgby= pcdy.colors[i*2048:]
                    while(len(nd)!=2048):
                        nd.append(nd[-1])
                        rgb.append(rgb[-1])
                        rgby.append(rgby[-1])
                else:
                    nd = pcd.points[i*2048:(i+1)*2048]
                    rgb = pcd.colors[i*2048:(i+1)*2048]
                    rgby = pcdy.colors[i*2048:(i+1)*2048]
                i+=1
                # RGB to YUV : 
                yuv_colors=[]
                yuv_y_colors=[]
                for clr in range(0,len(rgb)):
                    yuv_colors.append(rgb_to_yuv(rgb[clr]))
                    yuv_y_colors.append(rgb_to_yuv(rgby[clr]))                     
                # Graph signals
                xY = np.array(yuv_colors)[:,0]
                xU = np.array(yuv_colors)[:,1]
                xV = np.array(yuv_colors)[:,2]

                yY = np.array(yuv_y_colors)[:,0]
                yU = np.array(yuv_y_colors)[:,1]
                yV = np.array(yuv_y_colors)[:,2]



                temp_pcd = o3d.geometry.PointCloud()
                temp_pcd.points = nd
                # Adjacency Matrix
                a =  distance_matrix(nd , nd)
                a =   np.exp(-1*a)
                # a= sparse.csr_matrix(A)
                # Saving patches to files
                path = "/content/spektral/datasets/PatchDatasets"
                data_name= name.split('/')[-2]
                filenameY = os.path.join(path, f'graph_Y_{data_name}_{i}')
                filenameU = os.path.join(path, f'graph_U_{data_name}_{i}')
                filenameV = os.path.join(path, f'graph_V_{data_name}_{i}')
                np.savez(filenameY, x=xY, a=a, y=yY)


dataset = PatchDatasets()

"""## Model Creation/ Training : """

#          Parameters 
conv_layers =[512 , 256 , 128 , 64 , 1]
qps = [51 , 46 , 40 , 34]
# Learning Rate
lr=1e-5
# Batch
batch_size = 8
# Adam
beta1 = 0.9
beta2=0.999
# Inputs
F = 1 # Features
N= 2048 # Patch
split = int(0.8 * len(dataset))

def custom_loss_function(y_true, y_pred):
  squared_difference = tf.square(y_true - y_pred)
  return tf.reduce_mean(squared_difference, axis=-1)

class MyFirstGNN(Model):

    def __init__(self, n_channels, n_labels):
      super().__init__()
      self.graph_conv = ChebConv(channels=n_channels)
      self.graph_conv2 = ChebConv(channels=n_channels)
      self.gat_conv = GATConv(64)
      self.pool = GlobalSumPool()
      self.dense = Dense(n_labels, 'relu')

    def call(self, inputs):
      if len(inputs) == 2:
        x, a = inputs
      # Branch structure 
      out = self.graph_conv([x, a])
      out = self.gat_conv([out, a])
      out = self.graph_conv2([out, a])
      out = self.gat_conv([out, a])
      out = self.graph_conv2([out, a])
      # Dense Layers 
      out = self.pool(out)
      print(np.shape(out))
      out = self.dense(out)
      # Residual learning
      x_res = x[:,:,0]
      out = tf.keras.layers.Add()([out, x_res])
      return out

model = MyFirstGNN(64, dataset.n_labels)
opt = keras.optimizers.Adam(learning_rate=lr)
model.compile(optimizer=opt, loss=custom_loss_function)


split = int(0.8 * len(dataset))

data_tr, data_te = dataset[:split], dataset[split:]

loader_va = BatchLoader(data_te, batch_size=3)
loader_tr = BatchLoader(data_tr, batch_size=3)

model.fit(loader_tr.load(), steps_per_epoch=loader_tr.steps_per_epoch, epochs=50)

loss = model.evaluate(loader_va.load(), steps=loader_va.steps_per_epoch)
print('Test loss: {}'.format(loss))

