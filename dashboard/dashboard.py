import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


st.set_page_config(page_title="Proyek Analisis Data")
products_customer_orders_itemsorder_df = pd.read_csv(os.path.abspath('all_df.csv'))



st.write(
""" # Proyek Analisis Data E-Commerce Public Dataset"""
)

tab1, tab2, tab3 = st.tabs(["Jumlah Penjualan Menurut Kota", "Penjualan Produk Terbanyak", "Tren Penjualan dalam Setahun Terakhir"])

with tab1:
    st.header('Jumlah Penjualan Menurut Kota')
    
    city_customer = products_customer_orders_itemsorder_df.groupby("customer_city")

    sales_df = city_customer.price.sum().sort_values(ascending=False).reset_index()
    sales_df.rename(columns={
        "customer_city": "city"
    }, inplace=True)
    

    top_city_consumer = sales_df.head(8)
    colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        x="price", 
        y="city",
        data=top_city_consumer.sort_values(by="price", ascending=False),
        palette=colors_,
        hue=top_city_consumer['city']
    )

    plt.title("Number of Sales by City", loc="center", fontsize=15)
    plt.ylabel("City")
    plt.xlabel("Sales (\\$)")
    plt.tick_params(axis='y', labelsize=12)

    st.pyplot(plt)
    plt.clf() 

    st.write("Secara signifikan, Sao Paulo dan Rio de Janeiro melakukan pembelian yang lebih banyak dibandingkan kota-kota lain. Tepatnya senilai \\$1,859,556.83, disusul oleh Rio de Janeiro sebesar \\$955,573.97. Hal ini berarti e-commerce ini memiliki basis pembeli yang besar di Sao Paulo dan Rio de Janeiro.")
with tab2:
    st.header('Penjualan Produk Terbanyak')
    sales = products_customer_orders_itemsorder_df.groupby("product_category_name_english").price.sum().sort_values(ascending=False).reset_index()
    sales.rename(columns={
        "product_category_name_english": "Product Category",
        "price": "Price"
    }, inplace=True)

    top_product = sales.head(8)
    colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        x="Price", 
        y="Product Category",
        data=top_product,
        palette=colors_,
        hue=top_product['Product Category']
    )

    plt.title("Most Purchased Products", loc="center", fontsize=15)
    plt.ylabel("Product Category")
    plt.xlabel("Price (\\$)")
    plt.tick_params(axis='y', labelsize=12)

    st.pyplot(plt)
    plt.clf() 
    st.write("Secara berurutan, penjualan produk tidak berbeda jauh satu sama lain. Produk dengan kategori health beauty menyumbang penjualan yang paling banyak, yaitu sebesar \\$1,233,131.72. Kemudian disusul oleh Watches Gifts sebesar \\$1,165,898.98 dan bed_bath_table sebesar \\$1,023,434.76.")

with tab3:
    st.header('Tren Penjualan dalam Setahun Terakhir')
    monthly_trend = products_customer_orders_itemsorder_df.groupby("order_purchase_month").price.sum().reset_index()

    monthly_trend.rename(columns={
        "order_purchase_month": "month",
        "price": "revenue"
    }, inplace=True)

    # monthly_trend["month"] = monthly_trend["month"].dt.to_timestamp().dt.strftime('%Y-%m')
    latest_year = monthly_trend.tail(13)
    
    plt.figure(figsize=(10, 5))
    plt.plot(
        latest_year["month"],
        latest_year["revenue"],
        marker='o',
        linewidth=2,
        color="#72BCD4"
    )
    plt.title("Total Revenue 2017-08 to 2017-08", loc="center", fontsize=20)
    plt.xticks(fontsize=10, rotation=90)
    plt.yticks(fontsize=10)
    
    st.pyplot(plt)
    plt.clf()
    st.write("Secara garis besar, penjualan mengalami peningkatan selama setahun terakhir. Penjualan bulan Agustus 2018 sebesar \\$836,377.59, meningkat dibandingkan setahun sebelumnya yang bernilai \\$549,731.25. Namun, terjadi penurunan penjualan selama 3 bulan terakhir dengan nilai yang kurang lebih sama, yaitu \\$862,874.47 pada bulan Juli, \\$853,204.84 pada bulan Juni.")
