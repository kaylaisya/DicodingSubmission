import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

# Membuat tabel payments
payments_df = pd.read_csv("https://raw.githubusercontent.com/kaylaisya/submission/main/order_payments_dataset.csv")

# Membuat gambar dan sumbu untuk setiap histogram
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot histogram
payments_df['payment_sequential'].plot(kind='hist', bins=20, ax=axs[0], title='Distribusi Payment Sequential')
payments_df['payment_value'].plot(kind='hist', bins=20, ax=axs[1], title='Distribusi Payment Value')
payments_df['payment_installments'].plot(kind='hist', bins=20, ax=axs[2], title='Distribusi Payment Installments')

# Menyesuaikan tata letak
plt.tight_layout()

# Menampilkan plot gabungan
plt.show()

# Menghitung kuartil pertama dan ketiga untuk payment_installments
Q1_installments = payments_df['payment_installments'].quantile(0.25)
Q3_installments = payments_df['payment_installments'].quantile(0.75)

# Menghitung Interquartile Range untuk payment_installments
IQR_installments = Q3_installments - Q1_installments

# Menghitung nilai maksimum dan minimum untuk mendeteksi outlier pada payment_installments
maximum_installments = Q3_installments + (1.5 * IQR_installments)
minimum_installments = Q1_installments - (1.5 * IQR_installments)

# Membuat kondisi untuk outlier pada payment_installments
condition_lower_than_installments = payments_df['payment_installments'] < minimum_installments
condition_more_than_installments = payments_df['payment_installments'] > maximum_installments

# Mengganti outlier dengan nilai maksimum dan minimum pada payment_installments
payments_df.loc[condition_more_than_installments, 'payment_installments'] = maximum_installments
payments_df.loc[condition_lower_than_installments, 'payment_installments'] = minimum_installments

# ============================================================================================================
st.title('Explore Payments Dataset 💸🛍️✨')

page = st.sidebar.selectbox("Pilih halaman", ["Home", "Analisis Data Eksploratori", "Analisis Korelasi"])

if page == "Home":
    st.header("Welcome!")
    st.write(
        """
        Selamat datang di dasbor Explore  Payment Dataset! Dasbor interaktif ini akan memberikan
        wawasan tentang data pembayaran platform *e-commerce* di Brazil! Jelajahi berbagai aspek 
        kumpulann data, termasuk urutan pembayaran, nilai pembayaran, dan cicilan untuk mendapatkan
        pemahaman berharga tentang perilaku pembayaran pelanggan 🌟
        """
    )

    st.write('')
    st.write('')

    st.header("Tentang Data 📊")
    st.write(
        """
        Kumpulan data yang digunakan yaitu [Order Payments Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_order_payments_dataset.csv),
        terdiri dari beberapa kolom yaitu:
        - `order_id`: berisi pengidentifikasi unik suatu pesanan.
        - `payment_sequential`: berisi urutan pembayaran pesanan jika pelanggan membayar dengan lebih dari satu metode pembayaran.
        - `payment_type`: berisi metode pembayaran yang dipilih oleh pelanggan.
        - `payment installments`: berisi jumlah angsuran yang dipilih oleh pelanggan.
        - `payment_value`: berisi nilai transaksi.
        """
    )

    st.write('')
    st.write('')

    st.header("Metode yang Digunakan ⚙️")
    st.write('')
    st.subheader("Analisis Data Eksploratori (ADE) 🔭")
    st.write(
        """
        **Analisis Data Eksploratori (ADE)** adalah pendekatan ini dilakukan untuk menganalisis kumpulan data untuk merangkum karakteristik 
        utamanya, biasanya dengan visualisasi data. Dalam analisis ini, kita akan menjawab beberapa pertayaam yaitu:
    
        **1. Berapa rata-rata jumlah angsuran pembayaran yang dipilih pelanggan?**
        > berfokus pada pemahaman perilaku pembayaran dalam kumpulan data, memberikan wawasan tentang preferensi pelanggan dan 
        fleksibilitas pembayaran.
    
        **2. Berapa total nilai pembayaran untuk setiap jenis pembayaran, dan bagaimana perbandingannya dengan nilai pembayaran keseluruhan?**
        > memberikan informasi mengenai setiap jenis pembayaran terhadap total nilai pembayaran, membantu dalam menilai popularitas
        dan efektivitas berbagai metode pembayaran.
    
        **3. Berapa persentase pesanan yang dibayar penuh sekaligus (`payment_sequential` = 1) dan apa yang bisa kita lakukan untuk meningkatkan 
        atau mempertahankan persentase ini?**
        > memberikan wawasan tentang perilaku pelanggan dan preferensi pembayaran.
    
        **4. Bagaimana perbedaan nilai pembayaran berdasarkan jumlah angsuran pembayaran?**
        > membantu memahami perilaku pelanggan, preferensi, dana dampak opsi pembayararan terhadap keputusan pembelian.
    
        **5. Apakah ada korelasi antara jumlah angsuran pembayaran yang dipilih pelanggan dengan nilai pembayaran?**
        > memberikan wawasan lebih lanjut tentang perilaku belanja pelanggan dan preferensi pembayaran dalam kumpulan data.
        """
        )
    
    st.write('')
    st.subheader("Analisis Korelasi 🔗")
    st.write(
        """
        Analisis ini berguna untuk menentukan korelasi antara angsuran pembayaran dan nilai pembayaran untuk memahami bagaimana opsi pembayaran
        memengaruhi perilaku pembelian.
        """
    )
    
    st.write('')
    st.header("Mulai Ekplorasi ✨")
    st.write(
        """
        Untuk mulai menjelajahi kumpulan data, gunakan sidebar untuk memilih opsi analisis yang diminati.
        """
    )

elif page == "Analisis Data Eksploratori":
    st.header("Analisis Data Eksploratori (ADE) 🔭")
    
    st.subheader("1. Berapa rata-rata jumlah angsuran pembayaran yang dipilih pelanggan?")
    avg_installments = payments_df['payment_installments'].mean()
    st.write(f"> **Rata-rata jumlah pembayaran angsuran adalah {avg_installments:.2f}**")
    st.write('')
    st.write(
    """
    Dari informasi ini, kita mendapat wawasan bahwa pelanggan cenderung membayar dalam beberapa angsuran daripada membayar secara penuh. 
    Rata-rata jumlah 2,75 anguran atau sekitar 3 angsuran mungkin menunjukkan bahwa pelanggan memiliki preferensi untuk pembayaran berkala.
    
    Informasi ini dapat membantu perusahaan untuk menyesuaikan kebijakan pembayaran mereka, seperti menawarkan opsi angsuran yang 
    lebih fleksibel atau menyesuaikan penawaran harga agar lebih sesuai dengan preferensi pelanggan. Ini dapat membantu menarik lebih banyak
    pelanggan dan meningkatkan kepuasan pelanggan.
    
    Selain itu, dengan mengetahui rata-rata jumlah angsuran, perusahaan dapat mengoptimalkan perencanaan keuangan,
    seperti manajemen kas dan proyeksi pendapatan.
    """
    )
    
    st.write('')
    st.subheader("2. Berapa total nilai pembayaran untuk setiap jenis pembayaran, dan bagaimana perbandingannya dengan nilai pembayaran keseluruhan?")
    total_payment_value = payments_df.groupby('payment_type')['payment_value'].sum()
    total_payment_value = total_payment_value[total_payment_value.index != 'not_defined']

    st.write("> **Total nilai pembayaran untuk setiap jenis pembayaran:**")
    st.write(total_payment_value)
    
    plt.figure(figsize=(10, 6))
    total_payment_value.plot(kind='bar')
    plt.title('Total nilai pembayaran untuk setiap jenis pembayaran')
    plt.xlabel('Jenis Pembayaran')
    plt.ylabel('Total Nilai Pembayaran')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    st.pyplot()
    st.write('')
    st.write(
    """
    Dari grafik ini, kita bisa tahu bahwa credit card adalah metode pembayaran dengan total nilai pembayaran terbesar yaitu sekitar 10 juta.
    Sedangkan total nilai pembayaran terendah dimiliki oleh jenis pembayaran debit card. Secara keseluruhan, penggunaan kartu kredit paling
    populer di kalangan pelanggan.

    Dengan informasi ini, perusahaan e-commerce bisa menganalissi lebih lanjut mengapa kartu kredit sangat dominan. Perusahaan mungkin perlu
    mempertimbangkan strategi untuk meningkatkan penggunaan metode pembayaran lainnya. Atau perusahaan bisa mengembangkan promosi yang
    berhubungan dengan metode pembayaran yang paling sering digunakan.
    """
    )
    
    st.write('')
    st.subheader("3. Berapa persentase pesanan yang dibayar penuh sekaligus dan apa yang bisa kita lakukan untuk meningkatkan atau mempertahankan persentase ini?")
    full_payment_percentage = (payments_df['payment_sequential'] == 1).mean() * 100
    st.write('')
    st.write(f"> **Persentase pesanan dibayar penuh sekaligus adalah {full_payment_percentage:.2f}%**")
    st.write(
    """
    Tingkat pembayaran penuh yang tinggi (96,54%) menunjukkan bahwa sebagian besar pelanggan cenderung melakukan pembayaran langsung 
    secara penuh saat memesan produk. Ini bisa mencerminkan kenyamanan dan kemudahan proses pembayaran yang disediakan oleh platform.

    Untuk mempertahankan tingkat pembayaran penuh sekaligus yang tinggi, perusahaan dapat terus meningkatkan pengalaman pelanggan 
    dalam berbelanja online. Hal ini termasuk memastikan keamanan transaksi, kemudahan navigasi situs, serta pelayanan pelanggan yang 
    responsif. Perusahaan juga bisa mempertimbangkan untuk menawarkan opsi pembayaran yang beragam, e-wallet
    """
    )
    
    st.write('')
    st.subheader("4. Bagaimana perbedaan nilai pembayaran berdasarkan jumlah angsuran pembayaran?")
    avg_payment_value_by_installments = payments_df.groupby('payment_installments')['payment_value'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='payment_installments', y='payment_value', data=avg_payment_value_by_installments)
    sns.regplot(x='payment_installments', y='payment_value', data=avg_payment_value_by_installments, scatter=False, color='red')
    plt.title('Rata-rata Nilai Pembayaran vs. Jumlah Angsuran Pembayaran')
    plt.xlabel('Jumlah Angsuran Pembayaran')
    plt.ylabel('Rata-rata Nilai Pembayarane')
    plt.grid(True)
    st.write('')
    st.pyplot()
    st.write('')
    st.write(
    """
    Berdasarkan scatter plot, terlihat bahwa ada korelasi positif antara jumlah angsuran pembayaran dan rata-rata nilai pembayaran. 
    Ini berarti, semakin banyak jumlah angsuran pembayaran, semakin tinggi nilai pembayaran rata-ratanya.

    Garis tren ini dapat digunakan untuk memprediksi nilai pembayaran rata-rata berdasarkan jumlah angsuran. Hal ini berguna untuk 
    menginformasikan keputusan manajemen keuangan dan penentuan struktur pembayaran. Misalnya, dapat digunakan untuk menentukan apakah
    penggunaan cicilan lebih banyak akan meningkatkan rata-rata nilai pembayaran dan arus kas.
    """
    )
    
elif page == "Analisis Korelasi":
    st.header("Analisis Korelasi 🔗")
    st.write(
    """
    Sebelumnya, di Analisis Data Eksploratori (ADE), kita mendapat informasi ada indikasi korelasi positif antara jumlah 
    angsuran pembayaran dan rata-rata nilai pembayaran. Untuk memastikan ini, kita bisa melakukan analisis korelasi untuk
    memahami hubungan 2 hal tersebut lebih lanjut.
    """
    )
    
    st.write('')
    st.subheader("5. Apakah ada korelasi antara jumlah angsuran pembayaran yang dipilih pelanggan dengan nilai pembayaran?")
    st.write('')
    correlation = payments_df['payment_installments'].corr(payments_df['payment_value'])
    st.write(f"> **Korelasi antara angsuran pembayaran dengan nilai pembayaran: {correlation:.2f}**")
    st.write('')
    st.write(
    """
    Dari informasi yang diberikan, terdapat korelasi positif yang lemah antara kedua variabel tersebut. Korelasi sebesar 0,32 
    menunjukkan bahwa ada hubungan positif antara jumlah angsuran pembayaran yang dipilih oleh pelanggan dengan nilai pembayaran, 
    tetapi hubungan tersebut tidak terlalu kuat. Meskipun korelasinya lemah, adanya korelasi positif menunjukkan bahwa dalam 
    beberapa kasus, semakin tinggi jumlah angsuran pembayaran yang dipilih oleh pelanggan, semakin tinggi pula nilai pembayarannya. 
    Ini bisa mengindikasikan bahwa pelanggan yang memilih angsuran lebih banyak cenderung melakukan pembayaran dengan nilai yang lebih tinggi.
    
    Informasi ini dapat digunakan oleh perusahaan untuk mengambil langkah-langkah yang sesuai untuk meningkatkan penjualan, 
    memahami perilaku pelanggan, dan mengoptimalkan strategi pembayaran mereka.
    """
    )
