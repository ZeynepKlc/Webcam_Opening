## Threads
Threading, bir programın aynı anda birden fazla işi eş zamanlı olarak yürütmesini sağlayan bir işlem yöntemidir. Bir işlemci çekirdeğinde sadece bir iş parçacığı (thread) çalıştırılabilirken, threading ile birden fazla iş parçacığı aynı anda çalışabilir ve işlemci kaynaklarının daha verimli kullanılmasını sağlar.Threading, paralel programlama, çoklu işlem ve eşzamanlılık gibi alanlarda yaygın olarak kullanılır

### Traceback
Traceback, Python'da bir hata veya istisna oluştuğunda hatanın kaynağını, hatanın hangi dosya ve hangi satırda olduğunu takip etmek için kullanılan bir araçtır. Traceback, hatanın nerede başladığını ve hangi fonksiyonlardan geçildiğini izlemek için hatanın yığın izini (stack trace) sağlar.

### traceback.format_exc()
Mevcut bir hata için ayrıntılı bir traceback bilgisini bir dize olarak döndürür. Bu fonksiyon, hata oluştuğunda traceback bilgisini yakalayarak, hatanın yığın izini ve diğer ilgili ayrıntıları içeren bir dize oluşturur.
format_exc() fonksiyonu, hatanın nerede oluştuğunu, hangi fonksiyonlardan geçildiğini ve hatanın yığın izini hakkında ayrıntılı bilgiler sağlar. 

