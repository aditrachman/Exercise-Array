# Nomer 3 dengan opsi penghapusan data atau akhiri program

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

# Menampilkan hasil ringkasan data mahasiswa
while True:
    print("\n" + "=" * 50)  
    print("Result of Students Recap Data")
    for i, mhs_data in enumerate(mhs, start=1):
        print(f"{i}. {mhs_data['name']} lives in {mhs_data['address']}, they majored in {mhs_data['major']} with {mhs_data['specialization']} expertise.")

    # Menampilkan pilihan untuk menghapus data atau mengakhiri program
    print("\nWhat would you like to do?")
    print("1. Remove a student's data")
    print("2. End the program")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        # Meminta nomor mahasiswa yang ingin dihapus
        remove_index = int(input("Enter the number of the student you want to remove: ")) - 1
        if 0 <= remove_index < len(mhs):
            removed_student = mhs.pop(remove_index)
            print(f"\nRemoved {removed_student['name']}'s data.")
        else:
            print("\nInvalid student number.")
    elif choice == 2:
        print("\nProgram end.")
        break
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
