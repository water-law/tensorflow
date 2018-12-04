# tensorFlow
a project to learn TensorFlow.

# use python env

for windows and python3, you can use 
```
python3 -m venv env  # create a virtualenv python env.
 
or

pip install virtualenv

virtualenv -p python3 env
```
activate the virtualenv python env by using

```
.\env\Scripts\activate.bat
```


# install

for windows, Use CPU-Z software to see if the CPU Instruction Set.

if CPU support avx2 then `pip install .\CPU\avx2\tensorflow-1.12.0-cp36-cp36m-win_amd64.whl`,

else if  CPU support sse2 then `pip install .\CPU\sse2\tensorflow-1.12.0-cp36-cp36m-win_amd64.whl`.

the protobuf>3.6.0 get an error using tensorflow==1.12.0, you should use protobuf==3.6.0.

when using

```
pip install matplotlib
```

if ocurr an error

```
import _tkinter # If this fails your Python may not be configured for Tk
   ImportError: No module named _tkinter
```

then cd to python home path, execute

```
git clone https://github.com/water-law/tkinter.git
```

# run
```
python3 example1.py

python3 example2.py

python3 .\fully_connected_feed.py --log_dir logs --input_data_dir MNIST_data
```

# use tensorboard

when you install tensorflow, then tensorboard is also installed. when you use

```
python3 xxx.py

```

to run a python script, there create event file also, default the dictionary is

`logs dir. you can use make to start a tensorboard.

to use make, you maybe need to install `cgywin and the install `make library.

enter the dictionary Makefile in, run make command after you activate python virtualenv env.
