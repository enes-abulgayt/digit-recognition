#  English
#  Handwritten Digit Recognition (MNIST)

A simple **Streamlit web app** that recognizes handwritten digits (0–9) drawn by the user.  
The model is trained on the **MNIST dataset** using TensorFlow and Keras.

---

##  Features

-  Deep learning model built with TensorFlow/Keras  
-  Interactive drawing canvas (Streamlit Drawable Canvas)  
-  Live prediction results with probability chart  
-  Trained model saved as `mymodel.h5`

---

##  Model Architecture and Algorithms

This project uses a fully connected neural network (Dense Network) to classify handwritten digits from the MNIST dataset.  
Instead of using convolutional layers, the model flattens each 28×28 image into a 784-dimensional vector and passes it through several dense layers.

###  Architecture
- `Dense(256, relu)` – First hidden layer with 256 neurons  
- `Dropout(0.2)` – Regularization to prevent overfitting  
- `Dense(128, relu)` – Second hidden layer  
- `Dropout(0.2)` – Another regularization layer  
- `Dense(64, relu)` – Third hidden layer  
- `Dense(10, softmax)` – Output layer for digit classification

###  Training Details
- **Optimizer**: Adam  
- **Loss Function**: Sparse Categorical Crossentropy  
- **Epochs**: 10  
- **Batch Size**: 32  
- **Validation Split**: 10% of training data

###  Performance

The model achieves over **97% accuracy** on the MNIST test dataset.  
This high accuracy is due to the simplicity of the MNIST images and the effectiveness of dense neural networks for this classification task.

The trained model is saved as `mymodel.h5` and can be loaded for inference in the Streamlit app.

##  How to Run Locally

### 1️- Clone the repository
```bash
git clone https://github.com/enes-abulgayt/digit-recognition.git
cd digit-recognition
```

###  2️- Install dependencies
```bash
pip install -r requirements.txt
```

### 3-train the model
```bash
python3 run train.py
```

### 4- Run the app
```bash
streamlit run app.py
```

---

#  Türkçe
#  El Yazısı Rakam Tanıma (MNIST)

Kullanıcının çizdiği **0–9 arasındaki el yazısı rakamlarını** tanıyan basit bir **Streamlit web uygulaması**.  
Model, TensorFlow ve Keras kullanılarak **MNIST veri seti** üzerinde eğitilmiştir.

---

##  Özellikler

-  TensorFlow/Keras ile oluşturulmuş derin öğrenme modeli  
-  Etkileşimli çizim alanı (Streamlit Drawable Canvas)  
-  Canlı tahmin sonuçları ve olasılık grafiği  
-  Eğitilmiş model dosyası: `mymodel.h5`

---

##  Model Mimarisi ve Algoritmalar

Bu proje, MNIST veri kümesindeki el yazısı rakamları sınıflandırmak için tam bağlantılı bir sinir ağı (Dense Network) kullanır.  
Evrişimli katmanlar (CNN) yerine, model her 28×28 görüntüyü 784 boyutlu bir vektöre dönüştürür ve bunu birkaç yoğun (dense) katmandan geçirir.

###  Mimari
- `Dense(256, relu)` – 256 nöronlu ilk gizli katman  
- `Dropout(0.2)` – Aşırı öğrenmeyi önlemek için düzenleme katmanı  
- `Dense(128, relu)` – İkinci gizli katman  
- `Dropout(0.2)` – Bir başka düzenleme katmanı  
- `Dense(64, relu)` – Üçüncü gizli katman  
- `Dense(10, softmax)` – Rakam sınıflandırması için çıkış katmanı

###  Eğitim Detayları
- **Optimizasyon**: Adam  
- **Kayıp Fonksiyonu**: Sparse Categorical Crossentropy  
- **Epok Sayısı**: 10  
- **Batch Boyutu**: 32  
- **Doğrulama Bölmesi**: Eğitim verisinin %10'u

###  Performans
Model, test verisinde %97'nin üzerinde doğruluk elde eder.  
Eğitilen model `mymodel.h5` olarak kaydedilir ve Streamlit uygulamasında tahmin için kullanılabilir.


##  Yerel Olarak Çalıştırma

### 1️- Depoyu klonlayın
```bash
git clone https://github.com/enes-abulgayt/digit-recognition.git
cd digit-recognition
```

### 2️- Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 3- Modeli Eğit
```bash
python3 run train.py
```

### 4- Uygulamayı Başlat
```bash
streamlit run app.py
```
