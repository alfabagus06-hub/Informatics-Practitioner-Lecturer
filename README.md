## Deskripsi Proyek

Repositori ini berisi kumpulan proyek studi kasus yang disusun berdasarkan materi dari Informatics Practitioner Lecture Series. Setiap proyek dibuat sebagai bentuk penerapan konsep yang telah dipelajari, mulai dari analisis data, komputasi paralel, pemetaan geografis, machine learning, visualisasi data, hingga pemantauan perubahan lingkungan.

### 1. Data Analytics & AI — Analisis Produktivitas Belajar Mahasiswa

Proyek ini membahas analisis faktor-faktor yang berkaitan dengan produktivitas belajar mahasiswa. Data yang digunakan mencakup jam tidur, durasi belajar, dan tingkat kehadiran. Dengan menggunakan Python, Pandas, NumPy, Matplotlib, dan Streamlit, data diolah menjadi informasi yang lebih mudah dipahami melalui statistik sederhana, tabel, dan grafik.

Tujuan proyek ini adalah menunjukkan bagaimana proses analisis data dapat membantu memahami hubungan antarvariabel dan menghasilkan informasi yang berguna. Data yang digunakan bersifat sintetis sehingga hasilnya hanya digunakan untuk demonstrasi, bukan untuk menarik kesimpulan mengenai mahasiswa secara nyata.

### 2. High Performance Computing (HPC) — Perbandingan Pemrosesan Serial dan Paralel

Proyek ini membandingkan pemrosesan serial dan paralel dalam menyelesaikan perhitungan numerik menggunakan Python. Pemrosesan serial menjalankan perhitungan secara berurutan, sedangkan pemrosesan paralel membagi pekerjaan ke beberapa proses agar dapat dikerjakan secara bersamaan.

Implementasi dilakukan dengan mengukur waktu eksekusi kedua metode dan membandingkan hasil perhitungannya. Melalui proyek ini, pengguna dapat memahami konsep dasar komputasi paralel serta mengetahui bahwa pemrosesan paralel tidak selalu lebih cepat karena adanya overhead dan keterbatasan perangkat keras.

### 3. Geographic Information System (GIS) — Pemetaan Fasilitas Umum

Proyek ini menerapkan konsep Sistem Informasi Geografis (GIS) untuk menampilkan persebaran fasilitas umum pada peta interaktif. Data mencakup nama fasilitas, jenis fasilitas, serta koordinat lintang dan bujur.

Dengan menggunakan Python, Pandas, dan Streamlit, pengguna dapat melihat lokasi fasilitas pada peta, menyaring data berdasarkan kategori, dan memeriksa informasi dalam bentuk tabel. Proyek ini memperkenalkan pemanfaatan data spasial untuk menyajikan informasi lokasi secara visual. Koordinat yang digunakan masih berupa data simulasi, bukan hasil survei lapangan.

### 4. Machine Learning — Klasifikasi Kebutuhan Dukungan Belajar

Proyek ini menerapkan metode *Machine Learning* untuk mendemonstrasikan proses klasifikasi menggunakan data akademik simulasi. Fitur yang digunakan meliputi durasi belajar, tingkat kehadiran, dan persentase tugas yang diselesaikan.

Model Logistic Regression digunakan untuk mempelajari pola dari data latih dan menghasilkan prediksi pada data uji. Evaluasi dilakukan menggunakan akurasi, *classification report*, dan *confusion matrix*. Proyek ini bertujuan memperlihatkan tahapan dasar pengembangan model Machine Learning, mulai dari persiapan data hingga evaluasi hasil. Karena data dan label dibuat secara sintetis, hasil model tidak ditujukan untuk menilai mahasiswa sungguhan.

### 5. Human-Computer Interaction (HCI) & Data Visualization — Dashboard Kualitas Udara

Proyek ini berfokus pada penyajian informasi kualitas udara melalui dashboard interaktif. Data PM2.5 simulasi ditampilkan dalam bentuk ringkasan nilai, grafik garis, dan tabel yang dapat disaring berdasarkan lokasi serta rentang tanggal.

Dashboard dikembangkan menggunakan Python, Pandas, NumPy, Matplotlib, dan Streamlit. Dari sisi Human-Computer Interaction (HCI), proyek ini menekankan penyusunan informasi yang jelas, kontrol yang mudah digunakan, serta pesan yang membantu ketika data tidak tersedia untuk filter tertentu.

Tujuan proyek ini adalah menunjukkan bagaimana visualisasi data dan rancangan antarmuka dapat membantu pengguna memahami informasi dengan lebih mudah. Data yang digunakan bukan pengukuran kualitas udara secara langsung.

### 6. Pemantauan Perubahan Tutupan Hutan — Analisis Perbandingan Antarperiode

Proyek ini mengangkat konsep pemantauan perubahan tutupan hutan berdasarkan materi mengenai penggunaan citra satelit dan klasifikasi untuk mengamati perubahan lingkungan. Implementasi demonstrasi menggunakan tabel persentase tutupan hutan simulasi dari beberapa wilayah pada dua periode berbeda.

Data diolah menggunakan Python dan Pandas, kemudian ditampilkan dalam bentuk tabel dan grafik batang untuk memperlihatkan perbedaan nilai antarperiode. Proyek ini membantu menjelaskan bagaimana perubahan data dapat dianalisis dan disajikan secara visual.

Perlu diperhatikan bahwa implementasi ini belum memproses citra satelit secara langsung. Data yang digunakan hanya bersifat simulasi, sehingga hasilnya tidak dapat dianggap sebagai bukti terjadinya deforestasi di wilayah tertentu.

## Kesimpulan

Keenam proyek tersebut menunjukkan penerapan konsep informatika dalam beberapa bidang yang berbeda. Analisis data digunakan untuk memahami pola informasi, HPC untuk membandingkan pendekatan komputasi, GIS untuk memvisualisasikan lokasi, Machine Learning untuk mempelajari proses klasifikasi, HCI dan visualisasi data untuk meningkatkan kemudahan pemahaman informasi, serta pemantauan hutan untuk memperkenalkan analisis perubahan lingkungan.

Melalui kumpulan proyek ini, diharapkan pemahaman terhadap materi yang disampaikan oleh para pemateri dapat diperkuat melalui implementasi sederhana menggunakan Python. Setiap proyek masih dapat dikembangkan lebih lanjut dengan data nyata yang tervalidasi, metode analisis yang lebih sesuai, serta pengujian tambahan berdasarkan kebutuhan masing-masing studi kasus.
