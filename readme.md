# AI Chant Counter

The tool is used to count the number of chants the user has done, given the actual mantra and an audio input. 

It uses `openai-whisper` model for trascription of the audios. however the accuracy for **Hindi**  and **sanskrit** Recognition is very low. and this  is why overall count accuracy is very low and it is not reliable. 

The tool also implements a webscoket based fast api based server that takes audio to input in runtime and delivers timely count.


## Setup 

### Step-1 : Setup the codebase

```
git clone 
cd Chant-Counter
```
### Step-2 : Setup the env

With Conda
If you have Anaconda installed on your system, do the following to setup the env

```
conda env create -f envirnoment.yml
```

With Python

Install python version `3.12.2` and run the following command

```
pip  install -r requirements.txt
```

## Startup

Run the following command to start the FASTAPI server

```
uvicorn app:app --reload
```

## API Documentation