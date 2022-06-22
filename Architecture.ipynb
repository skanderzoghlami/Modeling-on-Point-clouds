{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "PC_To_Graph.ipynb",
      "provenance": [],
      "collapsed_sections": []
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
      "source": [
        "!pip install open3d scipy spektral"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xu2yWW5E1kgN",
        "outputId": "4f3e5815-6de1-40ff-b20f-d7ff159b3e93"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: open3d in /usr/local/lib/python3.7/dist-packages (0.15.2)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.7/dist-packages (1.4.1)\n",
            "Requirement already satisfied: spektral in /usr/local/lib/python3.7/dist-packages (1.1.0)\n",
            "Requirement already satisfied: jupyterlab==3.*,>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (3.4.3)\n",
            "Requirement already satisfied: matplotlib>=3 in /usr/local/lib/python3.7/dist-packages (from open3d) (3.2.2)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.7/dist-packages (from open3d) (4.64.0)\n",
            "Requirement already satisfied: wheel>=0.36.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (0.37.1)\n",
            "Requirement already satisfied: numpy>=1.18.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (1.21.6)\n",
            "Requirement already satisfied: pyyaml>=5.4.1 in /usr/local/lib/python3.7/dist-packages (from open3d) (6.0)\n",
            "Requirement already satisfied: pandas>=1.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (1.3.5)\n",
            "Requirement already satisfied: pygments>=2.7.4 in /usr/local/lib/python3.7/dist-packages (from open3d) (2.12.0)\n",
            "Requirement already satisfied: ipywidgets>=7.6.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (7.7.0)\n",
            "Requirement already satisfied: addict in /usr/local/lib/python3.7/dist-packages (from open3d) (2.4.0)\n",
            "Requirement already satisfied: setuptools>=40.8.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (62.6.0)\n",
            "Requirement already satisfied: jupyter-packaging~=0.10 in /usr/local/lib/python3.7/dist-packages (from open3d) (0.12.2)\n",
            "Requirement already satisfied: pyquaternion in /usr/local/lib/python3.7/dist-packages (from open3d) (0.9.9)\n",
            "Requirement already satisfied: scikit-learn>=0.21 in /usr/local/lib/python3.7/dist-packages (from open3d) (1.0.2)\n",
            "Requirement already satisfied: pillow>=8.2.0 in /usr/local/lib/python3.7/dist-packages (from open3d) (9.1.1)\n",
            "Requirement already satisfied: jinja2>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (3.1.2)\n",
            "Requirement already satisfied: jupyter-server~=1.16 in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (1.17.1)\n",
            "Requirement already satisfied: jupyter-core in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (4.10.0)\n",
            "Requirement already satisfied: tornado>=6.1.0 in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (6.1)\n",
            "Requirement already satisfied: jupyterlab-server~=2.10 in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (2.14.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (21.3)\n",
            "Requirement already satisfied: nbclassic~=0.2 in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (0.3.7)\n",
            "Requirement already satisfied: ipython in /usr/local/lib/python3.7/dist-packages (from jupyterlab==3.*,>=3.0.0->open3d) (5.5.0)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.6.0->open3d) (1.1.0)\n",
            "Requirement already satisfied: widgetsnbextension~=3.6.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.6.0->open3d) (3.6.0)\n",
            "Requirement already satisfied: traitlets>=4.3.1 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.6.0->open3d) (5.3.0)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.6.0->open3d) (5.4.0)\n",
            "Requirement already satisfied: ipykernel>=4.5.1 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.6.0->open3d) (4.10.1)\n",
            "Requirement already satisfied: ipython-genutils~=0.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.6.0->open3d) (0.2.0)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.7/dist-packages (from ipykernel>=4.5.1->ipywidgets>=7.6.0->open3d) (7.3.4)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython->jupyterlab==3.*,>=3.0.0->open3d) (4.4.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython->jupyterlab==3.*,>=3.0.0->open3d) (0.7.5)\n",
            "Requirement already satisfied: pexpect in /usr/local/lib/python3.7/dist-packages (from ipython->jupyterlab==3.*,>=3.0.0->open3d) (4.8.0)\n",
            "Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.7/dist-packages (from ipython->jupyterlab==3.*,>=3.0.0->open3d) (0.8.1)\n",
            "Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in /usr/local/lib/python3.7/dist-packages (from ipython->jupyterlab==3.*,>=3.0.0->open3d) (1.0.18)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.7/dist-packages (from jinja2>=2.1->jupyterlab==3.*,>=3.0.0->open3d) (2.0.1)\n",
            "Requirement already satisfied: deprecation in /usr/local/lib/python3.7/dist-packages (from jupyter-packaging~=0.10->open3d) (2.1.0)\n",
            "Requirement already satisfied: tomlkit in /usr/local/lib/python3.7/dist-packages (from jupyter-packaging~=0.10->open3d) (0.11.0)\n",
            "Requirement already satisfied: argon2-cffi in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (21.3.0)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (1.8.0)\n",
            "Requirement already satisfied: nbconvert>=6.4.4 in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (6.5.0)\n",
            "Requirement already satisfied: pyzmq>=17 in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (23.1.0)\n",
            "Requirement already satisfied: anyio<4,>=3.1.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (3.6.1)\n",
            "Requirement already satisfied: prometheus-client in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.14.1)\n",
            "Requirement already satisfied: terminado>=0.8.3 in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.13.3)\n",
            "Requirement already satisfied: websocket-client in /usr/local/lib/python3.7/dist-packages (from jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (1.3.3)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.7/dist-packages (from anyio<4,>=3.1.0->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (2.10)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from anyio<4,>=3.1.0->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (4.1.1)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.7/dist-packages (from anyio<4,>=3.1.0->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (1.2.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets>=7.6.0->open3d) (0.4)\n",
            "Requirement already satisfied: nest-asyncio>=1.5.4 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets>=7.6.0->open3d) (1.5.5)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets>=7.6.0->open3d) (2.8.2)\n",
            "Requirement already satisfied: importlib-metadata>=3.6 in /usr/local/lib/python3.7/dist-packages (from jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (4.11.4)\n",
            "Requirement already satisfied: babel in /usr/local/lib/python3.7/dist-packages (from jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (2.10.2)\n",
            "Requirement already satisfied: json5 in /usr/local/lib/python3.7/dist-packages (from jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (0.9.8)\n",
            "Requirement already satisfied: jsonschema>=3.0.1 in /usr/local/lib/python3.7/dist-packages (from jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (4.3.3)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (2.23.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=3.6->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (3.8.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0.1->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (0.18.1)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0.1->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (21.4.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0.1->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (5.7.1)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3->open3d) (3.0.9)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3->open3d) (0.11.0)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib>=3->open3d) (1.4.3)\n",
            "Requirement already satisfied: notebook<7 in /usr/local/lib/python3.7/dist-packages (from nbclassic~=0.2->jupyterlab==3.*,>=3.0.0->open3d) (5.3.1)\n",
            "Requirement already satisfied: notebook-shim>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from nbclassic~=0.2->jupyterlab==3.*,>=3.0.0->open3d) (0.1.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.7.1)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (4.6.3)\n",
            "Requirement already satisfied: tinycss2 in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (1.1.1)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (1.5.0)\n",
            "Requirement already satisfied: jupyterlab-pygments in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.2.2)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.8.4)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (5.0.0)\n",
            "Requirement already satisfied: nbclient>=0.5.0 in /usr/local/lib/python3.7/dist-packages (from nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.6.4)\n",
            "Requirement already satisfied: fastjsonschema in /usr/local/lib/python3.7/dist-packages (from nbformat>=4.2.0->ipywidgets>=7.6.0->open3d) (2.15.3)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=1.0->open3d) (2022.1)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython->jupyterlab==3.*,>=3.0.0->open3d) (0.2.5)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython->jupyterlab==3.*,>=3.0.0->open3d) (1.15.0)\n",
            "Requirement already satisfied: threadpoolctl>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from scikit-learn>=0.21->open3d) (3.1.0)\n",
            "Requirement already satisfied: joblib>=0.11 in /usr/local/lib/python3.7/dist-packages (from scikit-learn>=0.21->open3d) (1.1.0)\n",
            "Requirement already satisfied: ptyprocess in /usr/local/lib/python3.7/dist-packages (from terminado>=0.8.3->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.7.0)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.7/dist-packages (from spektral) (4.2.6)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.7/dist-packages (from spektral) (2.6.3)\n",
            "Requirement already satisfied: tensorflow>=2.2.0 in /usr/local/lib/python3.7/dist-packages (from spektral) (2.8.2+zzzcolab20220527125636)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (1.6.3)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (0.2.0)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (1.46.3)\n",
            "Requirement already satisfied: libclang>=9.0.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (14.0.1)\n",
            "Requirement already satisfied: flatbuffers>=1.12 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (2.0)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (0.26.0)\n",
            "Requirement already satisfied: keras<2.9,>=2.8.0rc0 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (2.8.0)\n",
            "Requirement already satisfied: absl-py>=0.4.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (1.1.0)\n",
            "Requirement already satisfied: tensorboard<2.9,>=2.8 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (2.8.0)\n",
            "Requirement already satisfied: opt-einsum>=2.3.2 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (3.3.0)\n",
            "Requirement already satisfied: wrapt>=1.11.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (1.14.1)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (1.1.0)\n",
            "Requirement already satisfied: keras-preprocessing>=1.1.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (1.1.2)\n",
            "Requirement already satisfied: gast>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (0.5.3)\n",
            "Requirement already satisfied: tensorflow-estimator<2.9,>=2.8 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (2.8.0)\n",
            "Requirement already satisfied: protobuf<3.20,>=3.9.2 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (3.17.3)\n",
            "Requirement already satisfied: h5py>=2.9.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow>=2.2.0->spektral) (3.1.0)\n",
            "Requirement already satisfied: cached-property in /usr/local/lib/python3.7/dist-packages (from h5py>=2.9.0->tensorflow>=2.2.0->spektral) (1.5.2)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (1.35.0)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (3.3.7)\n",
            "Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (1.8.1)\n",
            "Requirement already satisfied: werkzeug>=0.11.15 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (1.0.1)\n",
            "Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (0.6.1)\n",
            "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (0.4.6)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (0.2.8)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.7/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (4.8)\n",
            "Requirement already satisfied: cachetools<5.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (4.2.4)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.7/dist-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (1.3.1)\n",
            "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /usr/local/lib/python3.7/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (0.4.8)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (2022.6.15)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->jupyterlab-server~=2.10->jupyterlab==3.*,>=3.0.0->open3d) (1.24.3)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.9,>=2.8->tensorflow>=2.2.0->spektral) (3.2.0)\n",
            "Requirement already satisfied: argon2-cffi-bindings in /usr/local/lib/python3.7/dist-packages (from argon2-cffi->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (21.2.0)\n",
            "Requirement already satisfied: cffi>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from argon2-cffi-bindings->argon2-cffi->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (1.15.0)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.7/dist-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (2.21)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert>=6.4.4->jupyter-server~=1.16->jupyterlab==3.*,>=3.0.0->open3d) (0.5.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import open3d as o3d\n",
        "import tensorflow as tf\n",
        "import numpy as np\n",
        "import spektral\n",
        "from tensorflow.keras.layers import Dropout, Input\n",
        "from scipy.sparse import csr_matrix\n",
        "path =\"/content/patch_523.ply\""
      ],
      "metadata": {
        "id": "EEhU53uh1DV1"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pcd = o3d.io.read_point_cloud(path)\n",
        "pcd"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QXES3N9M1Q4n",
        "outputId": "b8f7846a-b630-48cd-8cf0-4cf0c3bacbdc"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "PointCloud with 2048 points."
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pcd_xyz = np.asarray(pcd.points)\n",
        "pcd_rgb = np.asarray(pcd.colors)\n",
        "full_pc = np.concatenate((pcd_xyz,pcd_rgb),axis=1)"
      ],
      "metadata": {
        "id": "vKMBze9c19Nj"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "A = csr_matrix(full_pc)\n",
        "A"
      ],
      "metadata": {
        "id": "AX17DITt5ho6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "379b8f17-4884-4aa1-f732-4490fb15d3aa"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<2048x6 sparse matrix of type '<class 'numpy.float64'>'\n",
              "\twith 12288 stored elements in Compressed Sparse Row format>"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "polynominal = spektral.utils.chebyshev_polynomial(csr_matrix(full_pc), 1 )"
      ],
      "metadata": {
        "id": "zQ4bTnQCQKRV"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#          Parameters \n",
        "conv_layers =[512 , 256 , 128 , 64 , 1]\n",
        "qps = [51 , 46 , 40 , 34]\n",
        "# Learning Rate\n",
        "lr=1e-5\n",
        "# Batch\n",
        "batch_size = 8\n",
        "# Adam\n",
        "beta1 = 0.9\n",
        "beta2=0.999\n",
        "# Inputs\n",
        "F = 6 # Features\n",
        "N= 2048 # Patch"
      ],
      "metadata": {
        "id": "fFlarNawYpZY"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Model definition\n",
        "x_in = Input(shape=(F,))\n",
        "a_in = Input((N,), sparse=True, dtype=object)"
      ],
      "metadata": {
        "id": "4-mK5mMIQbfw"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from spektral.layers import ChebConv\n",
        "from spektral.layers import GATConv\n",
        "from tensorflow.keras.regularizers import l2\n",
        "\n",
        "gc_1 = ChebConv(\n",
        "    64, K=1, activation=\"relu\", kernel_regularizer=l2(2.5e-4), use_bias=False\n",
        ")([x_in, a_in])\n",
        "\n",
        "gat_1 = GATConv(\n",
        "    64,\n",
        "    concat_heads=True,\n",
        "    activation=\"elu\",\n",
        "    kernel_regularizer=l2(2.5e-4),\n",
        "    attn_kernel_regularizer=l2(2.5e-4),\n",
        "    bias_regularizer=l2(2.5e-4),\n",
        ")([gc_1, a_in])\n",
        "\n",
        "gc_2 = ChebConv(\n",
        "    64, K=1, activation=\"relu\", kernel_regularizer=l2(2.5e-4), use_bias=False\n",
        ")([gat_1, a_in])\n",
        "\n",
        "gat_2 = GATConv(\n",
        "    64,\n",
        "    concat_heads=True,\n",
        "    activation=\"elu\",\n",
        "    kernel_regularizer=l2(2.5e-4),\n",
        "    attn_kernel_regularizer=l2(2.5e-4),\n",
        "    bias_regularizer=l2(2.5e-4),\n",
        ")([gc_2, a_in])\n",
        "\n",
        "gc_3 = ChebConv(\n",
        "    64, K=1, activation=\"relu\", kernel_regularizer=l2(2.5e-4), use_bias=False\n",
        ")([gat_2, a_in])\n",
        "\n",
        "conc = tf.keras.layers.Concatenate(axis=1)([gc_1 , gat_1,gc_2 , gat_2,gc_3])\n",
        "dense = tf.keras.layers.Dense(64)(conc)"
      ],
      "metadata": {
        "id": "FfAOHpmATxwW"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from tensorflow.keras.losses import CategoricalCrossentropy\n",
        "from tensorflow.keras.optimizers import Adam\n",
        "from tensorflow.keras.models import Model\n",
        "# Build model\n",
        "branch = Model(inputs=[x_in, a_in], outputs=dense)\n",
        "optimizer = Adam(lr=lr)\n",
        "branch.compile(\n",
        "    optimizer=optimizer,\n",
        "    loss=CategoricalCrossentropy(reduction=\"sum\"),  # To compute mean\n",
        "    weighted_metrics=[\"acc\"],\n",
        ")\n",
        "branch.summary()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rRySVP7OWd_F",
        "outputId": "5ccd6c75-e88e-4802-a2ee-1fc8424066df"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"model\"\n",
            "__________________________________________________________________________________________________\n",
            " Layer (type)                   Output Shape         Param #     Connected to                     \n",
            "==================================================================================================\n",
            " input_1 (InputLayer)           [(None, 6)]          0           []                               \n",
            "                                                                                                  \n",
            " input_2 (InputLayer)           [(None, 2048)]       0           []                               \n",
            "                                                                                                  \n",
            " cheb_conv (ChebConv)           (None, 64)           384         ['input_1[0][0]',                \n",
            "                                                                  'input_2[0][0]']                \n",
            "                                                                                                  \n",
            " gat_conv (GATConv)             (None, 64)           4288        ['cheb_conv[0][0]',              \n",
            "                                                                  'input_2[0][0]']                \n",
            "                                                                                                  \n",
            " cheb_conv_1 (ChebConv)         (None, 64)           4096        ['gat_conv[0][0]',               \n",
            "                                                                  'input_2[0][0]']                \n",
            "                                                                                                  \n",
            " gat_conv_1 (GATConv)           (None, 64)           4288        ['cheb_conv_1[0][0]',            \n",
            "                                                                  'input_2[0][0]']                \n",
            "                                                                                                  \n",
            " cheb_conv_2 (ChebConv)         (None, 64)           4096        ['gat_conv_1[0][0]',             \n",
            "                                                                  'input_2[0][0]']                \n",
            "                                                                                                  \n",
            " concatenate (Concatenate)      (None, 320)          0           ['cheb_conv[0][0]',              \n",
            "                                                                  'gat_conv[0][0]',               \n",
            "                                                                  'cheb_conv_1[0][0]',            \n",
            "                                                                  'gat_conv_1[0][0]',             \n",
            "                                                                  'cheb_conv_2[0][0]']            \n",
            "                                                                                                  \n",
            " dense (Dense)                  (None, 64)           20544       ['concatenate[0][0]']            \n",
            "                                                                                                  \n",
            "==================================================================================================\n",
            "Total params: 37,696\n",
            "Trainable params: 37,696\n",
            "Non-trainable params: 0\n",
            "__________________________________________________________________________________________________\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/keras/optimizer_v2/adam.py:105: UserWarning: The `lr` argument is deprecated, use `learning_rate` instead.\n",
            "  super(Adam, self).__init__(name, **kwargs)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "conc"
      ],
      "metadata": {
        "id": "xeSOngzDWyae",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5a74518f-2ee5-46fd-df61-4074c8d16cd9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<KerasTensor: shape=(None, 320) dtype=float32 (created by layer 'concatenate')>"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "C66oeDeSe6pn"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}