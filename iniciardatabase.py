from app import *


def add_productos():
    db.session.add(Producto(nombre='My Hero Academia - Mina Ashido Hero Suit', precio=164, descripcion='Ver. 1/8 Scale Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-my-hero-academia-mina-ashido-hero-suit-ver-1-8-scale-figure-28430739374124_180x.jpg?v=1623800242'))
    db.session.add(Producto(nombre='Fairy Tail - Lucy Heartfilia Pop Up Parade', precio=39, descripcion='(Aquarius Form Ver)', stock=15,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-fairy-tail-lucy-heartfilia-pop-up-parade-aquarius-form-ver-28430770208812_180x.jpg?v=1623799075'))
    db.session.add(Producto(nombre='Demon Slayer - Giyu Tomioka Buzzmode', precio=131, descripcion='Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/aniplex-pvc-scale-figures-demon-slayer-giyu-tomioka-buzzmode-figure-28395125669932_180x.jpg?v=1623269397'))
    db.session.add(Producto(nombre='Rent A Girlfiend - Ruka Sarashina', precio=49, descripcion='Nendoroid', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-nendoroids-rent-a-girlfiend-ruka-sarashina-nendoroid-28430778662956_180x.jpg?v=1623798594'))
    db.session.add(Producto(nombre='Sword Art Online Alicization - Yuuki', precio=164, descripcion='(Swimsuit Ver)', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-sword-art-online-alicization-yuuki-swimsuit-ver-28400658579500_180x.jpg?v=1623365122'))
    db.session.add(Producto(nombre='BOFURI: I Dont Want to Get Hurt, So Ill Max Out My Defense', precio=67, descripcion='Sally Nendoroid', stock=2,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-nendoroids-bofuri-i-don-t-want-to-get-hurt-so-i-ll-max-out-my-defense-sally-nendoroid-28400595206188_180x.jpg?v=1623362254'))
    db.session.add(Producto(nombre='Jujutsu Kaisen - Yuji Itadori Noodle Stopper', precio=24, descripcion='Figure', stock=30,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-jujutsu-kaisen-yuji-itadori-noodle-stopper-figure-28430754250796_360x.jpg?v=1623799791'))
    db.session.add(Producto(nombre='Re:Zero - Ram Figure ', precio=254, descripcion='Battle with Roswaal Ver', stock=5,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-re-zero-ram-figure-battle-with-roswaal-ver-28430719418412_180x.jpg?v=1623801476'))
    db.session.add(Producto(nombre='Black Rock Shooter - Black Rock Shooter', precio=40, descripcion='Pop Up Parade', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-black-rock-shooter-black-rock-shooter-pop-up-parade-28430584217644_180x.jpg?v=1623803162'))
    db.session.add(Producto(nombre='Date A Live III - Kurumi Tokizaki Figure', precio=204, descripcion='China Dress Ver', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-date-a-live-iii-kurumi-tokizaki-figure-china-dress-ver-28430799896620_180x.jpg?v=1623800774'))
    db.session.add(Producto(nombre='Is The Order A Rabbit? - Rize Figure', precio=169, descripcion='Military Uniform Ver', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-is-the-order-a-rabbit-rize-figure-military-uniform-ver-28430730690604_180x.jpg?v=1623800517'))
    db.session.add(Producto(nombre='Is The Order A Rabbit? - Cocoa Figure', precio=169, descripcion='Military Uniform Ver', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-is-the-order-a-rabbit-cocoa-figure-military-uniform-ver-28430726004780_180x.jpg?v=1623801204'))
    db.session.add(Producto(nombre='Laid-Back Camp - Nadeshiko Kagamihara', precio=20, descripcion='Laid-Back Camp - Nadeshiko Kagamihara', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-chibi-figures-laid-back-camp-nadeshiko-kagamihara-chobirume-figure-28395318706220_180x.jpg?v=1623275602'))
    db.session.add(Producto(nombre='Demon Slayer - Shinobu Kocho Hikkake', precio=20, descripcion='Ver. 1/8 Scale Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-chibi-figures-demon-slayer-shinobu-kocho-hikkake-figure-28395149066284_180x.jpg?v=1623269601'))
    db.session.add(Producto(nombre='Naruto Shippuden - Naruto Uzumaki', precio=164, descripcion='(New Package Ver) S.H.Figuarts', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/bluefin-pvc-scale-figures-naruto-shippuden-naruto-uzumaki-new-package-ver-s-h-figuarts-28434380783660_180x.jpg?v=1623893646'))
    db.session.add(Producto(nombre='The Idolmaster: Cinderella Girls - Yukimi', precio=209, descripcion='Sajo Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-the-idolmaster-cinderella-girls-yukimi-sajo-figure-28400617160748_180x.jpg?v=1623366322'))
    db.session.add(Producto(nombre='ODIN SPHERE LEIFDRASIR', precio=183, descripcion='GWENDOLYN DRESS VER. FIGURINE REPRODUCTION', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/02_a34a9eb7-ea96-4e10-aa95-c1cfc3dabc2f_large.jpg?v=1623928401'))
    db.session.add(Producto(nombre='Love Live! Superstar!! - Keke Tang SSS', precio=25, descripcion='Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/ultra-tokyo-connection-pvc-scale-figures-love-live-superstar-keke-tang-sss-figure-28395358257196_180x.jpg?v=1623272239'))
    db.session.add(Producto(nombre='Demon Slayer - Nezuko Kamado Exploding', precio=191, descripcion='Blood Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/aniplex-pvc-scale-figures-demon-slayer-nezuko-kamado-exploding-blood-figure-28037680496684_180x.jpg?v=1617061148'))
    db.session.add(Producto(nombre='Re:Zero - Frozen Emilia Figure', precio=164, descripcion='Crystal Dress Ver', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/cyberz-pvc-scale-figures-re-zero-frozen-emilia-figure-crystal-dress-ver-28187198685228_360x.jpg?v=1620241280'))
    db.session.add(Producto(nombre='Bushiroad Creative Shoujo Kageki Revue Starlight: Hikari Kagura ', precio=164,
                   descripcion='1: 7 escala PVC figura', stock=10, img_url='https://images-na.ssl-images-amazon.com/images/I/61wlEnJZNhL._AC_SY679_.jpg'))
    db.session.add(Producto(nombre='ATTACK ON TITAN THE FINAL SEASON-LEVI', precio=18, descripcion='', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/05_a85b2cd4-a501-4eaf-a7a0-e841d0fd60c2_large.jpg?v=1623723906'))
    db.session.add(Producto(nombre='DEMON SLAYER: KIMETSU NO YAIBA', precio=5116, descripcion='NEZUKO IN A BOX - BIG SIZE FIGURE', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/01_93ccb807-447f-4bab-bd78-e6555d810019_large.jpg?v=1618198500'))
    db.session.add(Producto(nombre='Overlord - Albedo Swimsuit', precio=579, descripcion='1/7 Scale Figure', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0014/2648/9388/products/cyberz-pvc-scale-figures-overlord-albedo-swimsuit-1-7-scale-figure-17403520253996_2000x2000.jpg?v=1606329454'))
    db.session.add(Producto(nombre='BINDING CREATORS OPINION AINA', precio=345, descripcion='BUNNY VERSION FIGURINE', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/02_91526006-3f99-4d4a-b2f6-5999fbfd2bec_large.jpg?v=1621827935'))
    db.session.add(Producto(nombre='DARLING IN THE FRANXX ZERO TWO', precio=320, descripcion='FOR MY DARLING FIGURINE', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/01_bcae9e59-5c7f-4a4d-be94-5f95d21dda78_large.jpg?v=1619413746'))
    db.session.add(Producto(nombre='SCHWARZESMARKEN IRISDINA', precio=150, descripcion='BERNHARD BUNNY VER. FIGURE', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/727dbc255979242728c63f4c5b893f3c_large.jpg?v=1472640814'))
    db.session.add(Producto(nombre='DEMON SLAYER: KIMETSU NO YAIBA BUZZMOD. GIYU TOMIOKA', precio=101, descripcion='FIGURINE', stock=10,
                   img_url='https://cdn.shopify.com/s/files/1/0367/9101/products/02_cd50acb7-67df-4387-b1c8-942afc0f10c2_large.jpg?v=1623074191'))


def insertar_categoria():
    db.session.add(Categoria(id=1, nombre='Plastic Model'))
    db.session.add(Categoria(id=2, nombre='Scale Figure'))
    db.session.add(Categoria(id=3, nombre='Action Figure'))
    db.session.add(Categoria(id=4, nombre='Figurine'))
    db.session.add(Categoria(id=5, nombre='Nendoroid'))
    db.session.add(Categoria(id=6, nombre='Other'))


def insertar_subcategoria():
    db.session.add(Subcategoria(id=1, nombre='Demon Slayer', categoria_id=1))
    db.session.add(Subcategoria(
        id=2, nombre='My Hero Academia', categoria_id=1))
    db.session.add(Subcategoria(
        id=3, nombre='Revue Starlight', categoria_id=1))
    db.session.add(Subcategoria(id=4, nombre='Re:Zero', categoria_id=2))
    db.session.add(Subcategoria(id=5, nombre='Fairy Tail', categoria_id=2))
    db.session.add(Subcategoria(id=6, nombre='BOFURI', categoria_id=2))
    db.session.add(Subcategoria(id=7, nombre='Jujutsu Kaisen', categoria_id=2))
    db.session.add(Subcategoria(
        id=8, nombre='Black Rock Shooter', categoria_id=2))
    db.session.add(Subcategoria(
        id=9, nombre='ATTACK ON TITAN', categoria_id=2))
    db.session.add(Subcategoria(id=10, nombre='Overlord', categoria_id=2))
    db.session.add(Subcategoria(
        id=11, nombre='SCHWARZESMARKEN', categoria_id=2))
    db.session.add(Subcategoria(id=12, nombre='ODIN SPHERE', categoria_id=4))
    db.session.add(Subcategoria(
        id=13, nombre='Rent A Girlfiend', categoria_id=5))
    db.session.add(Subcategoria(id=14, nombre='Overlord', categoria_id=2))
    db.session.add(Subcategoria(id=15, nombre='Re:Zero', categoria_id=3))
    db.session.add(Subcategoria(id=16, nombre='Demon Slayer', categoria_id=6))


def insertar_usuarios():
    # 4 admins
    db.session.add(Usuario(username='esteban', password='1234567', access=2, balance=0))
    db.session.add(Usuario(username='josedlz', password='1234567', access=2, balance=0))
    db.session.add(Usuario(username='pulsatio', password='1234567', access=2, balance=0))
    db.session.add(Usuario(username='elalien', password='1234567', access=2, balance=0))

    # 4 clientes
    db.session.add(Usuario(username='client1', password='1234567', access=1, balance=1000))
    db.session.add(Usuario(username='client2', password='1234567', access=1, balance=1000))
    db.session.add(Usuario(username='client3', password='1234567', access=1, balance=1000))
    db.session.add(Usuario(username='client4', password='1234567', access=1, balance=1000))


if __name__ == "__main__":
    db.create_all()
    insertar_usuarios()
    add_productos()
    insertar_categoria()
    insertar_subcategoria()
    db.session.commit()
