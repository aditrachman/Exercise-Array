#nomor 4 Program untuk memasukkan data mahasiswa dan menampilkan ringkasannya menggunakan array dua dimensi

# Meminta jumlah mahasiswa
num_mhs = int(input("Enter the number of students: "))

# Daftar untuk menyimpan data mahasiswa (menggunakan array dua dimensi)
mhs = []

# Memasukkan data setiap mahasiswa
for i in range(num_mhs):
    print(f"\nStudents {i + 1}:")
    name = input("Name: ")
    address = input("Address: ")
    major = input("Major: ")
    print("Gender List : \n 1.Male \n 2.female")
    gender = input("Gender List (enter 1 for male and 2 for female): ")
    specialization = input("Specialization: ")
    
    # Menambahkan data mahasiswa ke dalam array dua dimensi
    mhs.append([name, address, major, specialization, gender])

# Menampilkan hasil ringkasan data mahasiswa
print("\n" + "=" * 50)  
print("Result of Students Recap Data")
for i, student in enumerate(mhs, start=1):
    print(f"{i}. {student[0]} lives in {student[1]}, they majored in {student[2]} with {student[3]} expertise.")
