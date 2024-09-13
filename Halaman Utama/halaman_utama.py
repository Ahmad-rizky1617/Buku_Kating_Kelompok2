import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width=True, width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True 
        )
        st.markdown(
            """<div style="text-align: justify;">Cosval adalah singkatan dari cosine similiarity value, 
            dan dalam konteks kelompok kami, cosval memiliki pengertian bagaimanapun setiap anggota dari kelompok kami itu memiliki nilai 
            dan pandangannya masing-masing, kami tetap bersatu demi mencapai tujuan yang
            satu pula yaitu cosval yang satu dan bermaslahat.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1v3pP4xrpB-Wtot97192_Mltj4YCRE0Lf"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Cosval adalah kelompok 2 dari kaderisasi CEO HMSD dengan pendamping kelompok bernama bang rendi juga ka dea.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>Cosval Punya Cerita!!!</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17IHwnjun_lUPkqyYlOTA2c6rCzXMF6j1",
            "https://drive.google.com/uc?export=view&id=1akLNriez_lrmJ_NO_YbDSAHQ-DJQn2yj",
            "https://drive.google.com/uc?export=view&id=1Q7Rs5epvN8usr5QHfUNtfvdMJT6xhBjt",
            "https://drive.google.com/uc?export=view&id=1rjgDBRcs65bYxr8LvfZQDCxiXlbncldT",
            "https://drive.google.com/uc?export=view&id=1Aqc4h6KVwSWlbX-xHhJWkhBM_cAj85RC",
            "https://drive.google.com/uc?export=view&id=1YLCvZiZWUyio25SpYRddOKM9o7qMtEYS",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1KevS5s4qJh77sU3yNfkwMt8MUZBIwh98",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1p5c2pu-zlI6u9irYj_ipJfhA4J4E4FRu",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Km6LlwVy9XQMU9eBuMjrG2EcsgoX6G46",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1eGfyDbA8G4MauY8mf2xfC_DoBHFE13kv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

        ]
        data_list = [
            {
                "nama": "Ahmad Rizky",
                "sebagai": "Pak Lurah",
                "nim": "123450050",
                "fun_fact": "Sebenernya mau jadi pemain bola kaya lionel messi biar bisa bawa indonesia ke pildun",
                "motto_hidup": "now is now, then is then.",
            },
            {
                "nama": "Devyna Sonya Palupi Sanjaya",
                "sebagai": "Bu Lurah",
                "nim": "123450007",
                "fun_fact": "Dengerin lagu Bernadya 24/7",
                "motto_hidup": "everything happens for a reason",
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "sebagai": "Anggota",
                "nim": "123450048",
                "fun_fact": "softboy abizzzz",
                "motto_hidup": "kill the past",
            },
            {
                "nama": "Rahma Oktavia Albar",
                "sebagai": "Anggota",
                "nim": "123450003",
                "fun_fact": "pecinta mie ayam",
                "motto_hidup": "jangan pernah menyerah sebelum mencoba",
            },
            {
                "nama": "Intan Nursyabani",
                "sebagai": "Anggota",
                "nim": "123450081",
                "fun_fact": "tempe for life",
                "motto_hidup": "worst maybe could be the best, because almost everything is paradox",
            },
             {
                "nama": "Vania Claresta",
                "sebagai": "Anggota",
                "nim": "123450029",
                "fun_fact": "beli barang karena lucu",
                "motto_hidup": "with God all things are possible -Matthew 19:26",
            },
             {
                "nama": "G",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
             {
                "nama": "Malika Azzahra Salsabila",
                "sebagai": "Anggota",
                "nim": "123450090",
                "fun_fact": "Minum kopi biar bisa tidur",
                "motto_hidup": "When life gives you lemons, don't make lemonade. Make life take the lemons back.",
            },
             {
                "nama": "Ken Gracya Waoma",
                "sebagai": "Anggota",
                "nim": "123450045",
                "fun_fact": "lebih memprioritaskan untuk beristrahat",
                "motto_hidup": "all progress takes place outside the comfort zone",
            },
             {
                "nama": "Rahmah Gustriana Deka",
                "sebagai": "Anggota",
                "nim": "123450102",
                "fun_fact": "suka lupa tempat parkirin motor",
                "motto_hidup": "Be greather than averange",
            },
             {
                "nama": "Keren Marito Lumban Gaol",
                "sebagai": "Anggota",
                "nim": "123450020",
                "fun_fact": "suka makan telur",
                "motto_hidup": "Do Good, Receive Good",
            },
             {
                "nama": "L",
                "sebagai": "Anggota",
                "nim": "122450100",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
