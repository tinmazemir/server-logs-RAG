# server-logs-RAG 
# secureComputing task 

## ' streamlit run chat_interface.py ' (kullanici arayuzu ile sistemi calistirir)
## Dosya Sistemi 
### Src 
 * generate_logs.py (loglari olusturma fonksiyonlarini icerir)
 * manipulate_logs.py  (loglari temizler ve detaylandirmak icin yeni datalar ureten fonksiyonlari icerir)
 * create_store_vectors.py (uretilen loglari vectore ceviren ve depolayan fonksiyonlari icerir)
 * main_data.py (yukaridaki fonksiyonlarin senkron calistigi ana veri uretme ve depolama fonksiyonu)

 * search_index.py (vector veritabanindan verileri arama ve eslestirme fonksiyonlari)
 * answer_with_chatgpt.py (eslestirilen verileri baz alarak LLM ile metin uretme fonksiyonlari)
 * chat_interface.py (kullanici ile etkilesime gecme fonksiyonlari)

 * API_KEYS.py
 * RAG.ipynb (google colabs uzerinde hizli veri uretimi icin notebook)
### data
  * GeoLite2-City.mmdb (city ve country metadatasi uretilirken kullanilan veri)
  * enriched_logs.json (loglarin ve vectorlarin json dosyasi)
  * index.index (vector veritabani)
  

