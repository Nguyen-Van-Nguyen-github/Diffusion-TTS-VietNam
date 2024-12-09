# Diffusion-TTS-VietNam
## Cài Đặt
Tôi sử dụng môi trường Python 3.8.0 và Card đồ họa nvidia RTX A4000 cho toàn bộ quá trình huấn luyện.

```
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

Khởi tạo `monotonic_align` code (Cython):

```
cd model/monotonic_align; python setup.py build_ext --inplace; cd ../..
```

## Suy Luận
    ```
    python inference.py -f <your-text-file> -c <grad-tts-checkpoint> -t <number-of-timesteps> -s <speaker-id-if-multispeaker>
    python .\inference.py -f .\int_txt\input.txt -c .\checkpts\grad_1000.pt -t 20
    ```
4. Kiểm tra thư mục out

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
