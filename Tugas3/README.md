# Tugas-3-Progjar-E

```
Nama: Natasha Valentina
NRP: 05111640000183
Kelas : Pemrograman Jaringan E
```

Tugas 3:
- TCP File Server
- Client bisa request file (dan client dapat request file yang berada dalam folder)
- Client dapat memasukkan file ke server

Cara menjalankan:
1. Buka folder server, jalankan **fileServer.py**
2. Buka folder client, jalankan **fileClient.py**
3. Untuk mengetahui isi direktori gunakan perintah
`list [args] contoh: list . atau list images`
4. Untuk merequest file dari server ke client
`download [filename] contoh: download birthday.jpg atau download images/pie.jpg`
nama baru yang ada di client adalah : _client\_[filename]_
5. Untuk mengupload file dari client ke server
`upload [filename] contoh: upload pie.jpg`
nama baru yang ada di server adalah : _server\_[filename]_