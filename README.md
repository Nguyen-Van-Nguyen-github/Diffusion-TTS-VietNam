# Diffusion-TTS-VietNam
## Installation

Firstly, install all Python package requirements:

```bash
pip install -r requirements.txt
```

Secondly, build `monotonic_align` code (Cython):

```bash
cd model/monotonic_align; python setup.py build_ext --inplace; cd ../..
```

**Note**: code is tested on Python==3.8.0.

## Inference
    ```bash
    python inference.py -f <your-text-file> -c <grad-tts-checkpoint> -t <number-of-timesteps> -s <speaker-id-if-multispeaker>
    python .\inference.py -f .\int_txt\input.txt -c .\checkpts\grad_1000.pt -t 20
    ```
4. Check out folder called `out` for generated audios.

## Training

1. Make filelists of your audio data like ones included into `resources/filelists` folder. For single speaker training refer to `jspeech` filelists and to `libri-tts` filelists for multispeaker.
2. Set experiment configuration in `params.py` file.
3. Specify your GPU device and run training script:
    ```bash
    export CUDA_VISIBLE_DEVICES=YOUR_GPU_ID
    python train.py  # if single speaker
    python train_multi_speaker.py  # if multispeaker
    ```
4. To track your training process run tensorboard server on any available port:
    ```bash
    tensorboard --logdir=YOUR_LOG_DIR --port=8888
    ```
    During training all logging information and checkpoints are stored in `YOUR_LOG_DIR`, which you can specify in `params.py` before training.

## References

* HiFi-GAN model is used as vocoder, official github repository: [link](https://github.com/jik876/hifi-gan).
* Monotonic Alignment Search algorithm is used for unsupervised duration modelling, official github repository: [link](https://github.com/jaywalnut310/glow-tts).
* Phonemization utilizes CMUdict, official github repository: [link](https://github.com/cmusphinx/cmudict).
