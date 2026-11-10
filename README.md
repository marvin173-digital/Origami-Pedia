# OrigamiPedia

Katalog tutorial origami berbasis web dengan filter tingkat kesulitan
dan panduan langkah demi langkah. Dibuat untuk UTS Cloud Services (COMP6991031).

## Deskripsi dan alasan proyek
Tutorial origami biasanya tersebar di video dan blog sehingga pemula sulit menemukan panduan yang berurutan dan sesuai level. OrigamiPedia mengumpulkannya dalam satu katalog dengan filter tingkat kesulitan (mudah, sedang, sulit). Selain memecahkan masalah pengorganisasian konten, proyek statis ini sengaja dipilih sebagai sarana ideal untuk melatih perancangan arsitektur aplikasi 3-tier yang diorkestrasi menggunakan Docker Compose. Penguasaan infrastruktur backend yang stabil ini menjadi pondasi krusial yang selaras dengan tujuan karier saya di irisan Cloud Engineering dan Artificial Intelligence, khususnya untuk kebutuhan deployment model ke tahap produksi.

## Arsitektur
- `app`: Flask + Gunicorn, port 8000 (frontend dan backend)
- `db`: PostgreSQL 16, data disimpan di named volume `pgdata`, tidak dibuka ke host
- `adminer`: antarmuka database, hanya aktif di profile `tools`, port 8081
- Network: `origami-net`

![Diagram arsitektur](docs/architecture.png)

## Endpoint
| Method | Path | Fungsi | Status |
|---|---|---|---|
| GET | /health | Cek aplikasi | 200 |
| GET | /origami | Daftar origami (`?difficulty=mudah`) | 200 |
| POST | /origami | Tambah origami (`image` opsional) | 201 / 400 |
| GET | / | Halaman web katalog | 200 |

## Cara menjalankan
```bash
git clone https://github.com/marvin173-digital/Origami-Pedia.git
cd Origami-Pedia
cp .env.example .env        # PowerShell: copy .env.example .env
docker compose up -d --build
```
Buka http://localhost:8000. Untuk Adminer:
`docker compose --profile tools up -d`, lalu buka http://localhost:8081.

## Screenshot
![Tampilan aplikasi](docs/app-browser.png)
![Ukuran image](docs/docker-images.png)
![docker compose ps dan uji endpoint](docs/compose-ps-endpoint-test.png)
![Uji persistensi](docs/persistence.png)
![Adminer](docs/login-adminer.png)

## Sumber dan atribusi
- Library dan tools open-source: Flask, Gunicorn, psycopg2, PostgreSQL, dan Adminer.
- Gambar origami di `static/images/`:
  - Rabbit: https://www.thecraftfantastic.co.uk/tutorials/
  - Turtle: https://www.facebook.com/SarjigamiOrigamiArt/posts/origami-sea-turtle-tutorial-is-available-now/1528111386027542/
  - Naga : https://www.gathered.how/papercraft/origami/easy-origami-dragon-tutorial
  - boat : https://www.youtube.com/watch?v=khuVGbCE0PY
  - crane : https://web-japan.org/kidsweb/virtual/origami/exploring02f.html
- Teks langkah tutorial ditulis sendiri.

## Tautan
- Artikel: https://dev.to/marvino/origamipedia-building-a-multi-tier-app-with-docker-compose-2kej
- Video: https://youtu.be/3tUQnIgfwqQ

## AI Usage Declaration
- **Alat:** Claude (Anthropic), dan Gemini
- **Bagian yang dibantu AI:**
  - Brainstorming topik dan penyempitan fitur inti
  - Kerangka jawaban Soal 1
  - Kerangka `app.py`, `requirements.txt`, dan `index.html` dibantu Claude. Saya menempelkan kodenya ke proyek, menjalankannya, dan mengujinya sendiri.
  - `Dockerfile`, `.dockerignore`, dan `docker-compose.yml` dibantu Claude. Saya menjalankan dan menguji semuanya, dan akan menjelaskan tiap barisnya di video.
  - Diagram arsitektur (draf visual)
  - Panduan perintah terminal (Git, Docker, curl) dan debugging error: port 8080 bentrok, kesalahan YAML, login Adminer
- **Contoh prompt utama:**
  1. "kalau aku bikin proyek web aja kalau web buat tutorial semua kertas origami gmn?"
  2. "sekarang buatkan arsitektur diagram"
  3. "bisa tolong tambahin ini diwebsite gmn caranya?"
  4. Menempelkan pesan error terminal dan bertanya cara memperbaikinya
**Bagian yang saya kerjakan sendiri:**
  - Memilih topik dan menentukan fitur inti
  - Menjalankan semua perintah di terminal (Git, Docker, curl) serta pengujian dan screenshot
  - Menerapkan dan memperbaiki konfigurasi sampai berjalan: mengubah port Adminer yang bentrok di `docker-compose.yml` dan memperbaiki error YAML (diagnosis dibantu Claude)
  - Menulis langkah tutorial origami di database dan menyiapkan gambar
  - Menulis video, artikel, dan penjelasan di laporan 