{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Graph_creation.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jur-9hlC-Y_-"
      },
      "outputs": [],
      "source": [
        "!pip install open3d scipy"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import open3d as o3d\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "u7dNT6W_AK0B"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def distance(xi,xj):\n",
        "  return np.exp(-1* np.linalg.norm(xi-xj))"
      ],
      "metadata": {
        "id": "p-zODCJnAONg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Adjacency Matrix\n",
        "def pc_to_adj(pcd):\n",
        "  A=[]\n",
        "  for i in pcd.points:\n",
        "    row=[]\n",
        "    for j in pcd.points:\n",
        "      row.append(distance(i,j))\n",
        "    A.append(row)\n",
        "  return A"
      ],
      "metadata": {
        "id": "qJwpF62EAp2Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pcd = o3d.io.read_point_cloud(\"/content/patch_1.ply\")\n",
        "A= pc_to_adj(pcd)"
      ],
      "metadata": {
        "id": "--tTnhUtAvpw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Degree Matrix\n",
        "def adj_to_d(A):\n",
        "  D=np.zeros([2048,2048])\n",
        "  s=np.sum(np.asarray(A),axis=0)\n",
        "  for i in range(0,2048):\n",
        "    D[i][i]=np.sum(s[i])\n",
        "  return D"
      ],
      "metadata": {
        "id": "BG-jFtSCBpk8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Degree Matrix\n",
        "D= adj_to_d(A)"
      ],
      "metadata": {
        "id": "iaqm3ZyWBqRw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Graph laplacian \n",
        "Lc = D - A"
      ],
      "metadata": {
        "id": "RmxfWkBSD1Ob"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}