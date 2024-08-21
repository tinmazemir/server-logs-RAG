# Bitiş tarihi: 22 Ağustos Pazartesi:
# Kod Repository: Github 
# Ödev: Web Trafik Loglarına Dayalı Yapay Zeka Destekli Soru-Cevap Sistemi Geliştirme
# 1. Giriş:
   Bu projede, bir web sitesi için oluşturulan trafik loglarını kullanarak bir soru-cevap (Q&A) sistemi geliştirmeniz istenmektedir. Bu sistem, kullanıcılardan gelen doğal dildeki soruları alacak, ilgili log verilerini analiz edecek ve bu verilerle en uygun yanıtları oluşturacaktır. Sistemin temelinde Retrieval-Augmented Generation (RAG) modeli yer alacaktır.
   Ödevdeki tüm veri ödevin bir parçası olarak ödevi yapan tarafından üretilmelidir.
# 2. Proje Adımları:
  ## Aşama 1: Veri Hazırlığı ve Ön İşleme
      * Size verilen web trafik log dosyasını (örneğin, Apache/Nginx logları) anlayın ve analiz edin.
      * Log dosyasındaki gerekli verileri seçin, temizleyin ve yapılandırın (örneğin, IP adresleri, erişilen  sayfalar, zaman damgaları gibi verileri ayıklayın).
      * Bu log verilerini vektörlere dönüştürüp, uygun bir vektör veri tabanına (örneğin, FAISS, Pinecone) yükleyin.
   ## Aşama 2: RAG Modelinin Kurulumu
      * Retrieval-Augmented Generation (RAG) modelini kurun. Bu model iki ana bileşenden oluşur: bilgi alma (retrieval) ve jeneratif model (generation).
      * Bilgi Alma: Vektör veri tabanını kullanarak, kullanıcı sorusuna en uygun log kayıtlarını bulun.
      * Jeneratif Model: Bulduğunuz log kayıtlarını kullanarak, kullanıcının sorusuna uygun bir yanıt oluşturmak için bir dil modeli (örneğin, GPT, T5) kullanın.
   ## Aşama 3: Sistem Entegrasyonu ve Test
      * Bilgi alma ve jeneratif modeli birleştirerek entegre bir sistem oluşturun.
      * Kullanıcıdan gelen bir soruya yanıt verebilen, çalışan bir sistem tasarlayın.
      * Sistem, kullanıcı sorusunu aldıktan sonra vektör veri tabanında arama yapmalı, en uygun log kayıtlarını bulmalı ve bu kayıtları kullanarak dil modelinden bir yanıt oluşturmalıdır.
   ## Aşama 4: Performans Değerlendirmesi
      * Geliştirdiğiniz sistemin doğruluğunu ve performansını değerlendirin.
      * Sistemin cevaplarının kalitesini artırmak için hangi iyileştirmelerin yapılabileceğini düşünün ve bu konuda önerilerde bulunun.
# 3. Teslimat:
   * Geliştirdiğiniz sistemin kodları, anlaşılır ve belgelenmiş olmalıdır.
   * Sistem, size verilen log verileri üzerinde çalışır durumda olmalıdır.
   * Rapor: Proje boyunca izlediğiniz adımları ve karşılaştığınız zorlukları açıklayan detaylı bir rapor sunmalısınız. Ayrıca, sisteminizin performansı ve doğruluğu hakkında bir değerlendirme yapmalısınız.
# 4. Değerlendirme Kriterleri:
   * Veri İşleme Yetkinliği: Log verilerinin başarılı bir şekilde temizlenmesi ve vektör veri tabanına yüklenmesi.
   * Model Entegrasyonu: RAG modelinin doğru bir şekilde entegre edilmesi ve çalıştırılması.
   * Sonuçların Doğruluğu: Sistem tarafından üretilen cevapların doğruluğu ve kalitesi.
   * Raporlama: Proje raporunun netliği, analitik derinliği ve önerilen iyileştirmeler.