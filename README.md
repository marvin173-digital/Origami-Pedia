# OrigamiPedia

Katalog tutorial origami berbasis web dengan filter tingkat kesulitan
dan panduan langkah demi langkah. Dibuat untuk UTS Cloud Services (COMP6991031).

## Deskripsi dan alasan proyek
[Tulis 2-3 kalimat: masalah yang diselesaikan dan alasanmu memilih proyek ini]

## Arsitektur
- `app`: Flask + Gunicorn, port 8000 (frontend dan backend)
- `db`: PostgreSQL 16, data disimpan di named volume `pgdata`, tidak dibuka ke host
- `adminer`: antarmuka database, hanya aktif di profile `tools`, port 8081
- Network: `origami-net`

[Tempel diagram arsitektur di sini]

## Endpoint
| Method | Path | Fungsi | Status |
|---|---|---|---|
| GET | /health | Cek aplikasi | 200 |
| GET | /origami | Daftar origami (`?difficulty=mudah`) | 200 |
| POST | /origami | Tambah origami | 201 / 400 |

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
[Pasang screenshot dari folder docs/]

## Sumber dan atribusi
Flask, Gunicorn, psycopg2, PostgreSQL, dan Adminer (semuanya open-source).

## Tautan
- Artikel: [isi nanti]
- Video: [isi nanti]

## AI Usage Declaration
- Alat: Claude (Anthropic)
- Bagian yang dibantu: [sebutkan jujur: kerangka jawaban Soal 1, kerangka kode app.py, Dockerfile, docker-compose.yml, debugging error port dan YAML]
- Contoh prompt utama: [tulis 2-3 prompt yang benar-benar kamu ketik]
- Bagian yang saya kerjakan sendiri: [isi: misalnya pengujian, screenshot, penyesuaian, penjelasan di video]