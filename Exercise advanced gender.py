
# Nomer 2 dengan tambahan gender namun di output tidak di tampilkan

# Meminta jumlah mahasiswa
num_mhs = int(input("Enter the number of students: "))

# Daftar untuk menyimpan data mahasiswa
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
    mhs.append({
        "name": name,
        "address": address,
        "major": major,
        "specialization": specialization,
        "gender": gender
    })

# Menampilkan hasil ringkasan data mahasiswaa
print("\n" + "=" * 50)  
print("Result of Students Recap Data")
for i, mhs in enumerate(mhs, start=1):
    print(f"{i}. {mhs['name']} lives in {mhs['address']}, they majored in {mhs['major']} with {mhs['specialization']} expertise.")