# Diffusion-TTS-VietNam
Đây là dự án chuyển đổi văn bản thành giọng nói sử dụng diffusion và hifi-gan. Mô hình này được tham khảo bởi mô hình được nhóm tác giả ở huawei lab nghiên cứu. LICENSE mình có để trong mô hình các bạn tham khảo nhé.
Dự án còn phát triển tích cực cho multi speaker và đang cải thiện âm thanh cho phù hợp với ngôn ngữ vùng miền tại việt nam.
mọi đóng góp hay góp ý cho dự án vui lòng liên hệ: nguyenvannguyen192402@gmail.com

-[âm thanh nguồn](audio-source/audio-source.wav)
-[âm thanh sinh](out/)
-[text](input/)

## Cài Đặt
Tôi sử dụng môi trường Python 3.8.0 và Card đồ họa nvidia RTX A4000 cho toàn bộ quá trình huấn luyện.

```
python -m venv venv
venv/Scripts/activate
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

Khởi tạo `monotonic_align` code (Cython):

```
cd model/monotonic_align; python setup.py build_ext --inplace; cd ../..
```
## Tải model huấn luyện sẵn cho giọng Nữ
[Diffusion-TTS-Vietnam](https://drive.google.com/drive/folders/1K38bXWba7zC-mJ42Hf1QloWyG8BNnFDj?usp=sharing)
Đặt vào thư mục: checkpts (file grad_1000.pt)
[HiFi-Gan-Vietnam](https://drive.google.com/file/d/1fnvoRd_VCC-Me97j_EUSLOFwA86VgSyY/view?usp=sharing)
Đặt vào thư mục: checkpts (file g_00300000)

## Tải model huấn luyện sẵn cho giọng Nam
[Diffusion-TTS-Vietnam](https://drive.google.com/file/d/1ele07_tHl9fczekAuTXMLV51dsoV5ja4/view?usp=sharing)
Đặt vào thư mục: checkpts (file grad_641.pt)
[HiFi-Gan-Vietnam](https://drive.google.com/file/d/1MipWBU31V9s-aQ-1tcbUjhQswlhBk8vg/view?usp=sharing)
Đặt vào thư mục: checkpts (file g_00425000)

## Suy Luận
    ```
    python inference.py -f <your-text-file> -c <grad-tts-checkpoint> -t <number-of-timesteps> -s <speaker-id-if-multispeaker>
    python .\inference.py -f .\int_txt\input.txt -c .\checkpts\grad_1000.pt -t 20
    ```
4. Kiểm tra thư mục out

## Training
Tham Khảo dự án này, mình đã đựa vào nó để huấn luyện cho tiếng việt, dự án ban đầu được huấn luyện cho tiếng anh.
[Diffusion-Grad-TTS](https://github.com/huawei-noah/Speech-Backbones/tree/main/Grad-TTS)

## References

* HiFi-GAN model is used as vocoder, official github repository: [link](https://github.com/jik876/hifi-gan).
* Monotonic Alignment Search algorithm is used for unsupervised duration modelling, official github repository: [link](https://github.com/jaywalnut310/glow-tts).
* Phonemization utilizes CMUdict, official github repository: [link](https://github.com/cmusphinx/cmudict).
