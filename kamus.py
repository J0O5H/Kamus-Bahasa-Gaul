meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            'ROFL': 'Tanggapan terhadap lelucon',
            'SHEESH': 'sedikit ketidaksetujuan',
            'CREEPY': 'menakutkan',
            'AGGRO' : 'untuk menjadi agresif'
            }
            
            

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print('ARTINYA:')
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('MAAF KATA BELUM TERSEDIA/BELUM DI UPDATE')
