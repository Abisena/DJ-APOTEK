from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from django.contrib import messages

# Create your views here.
def medicine(request):
    medicine = Medicine.objects.all()
    return render(request, 'medicine/medicine.html', {'medicine': medicine})

def create_medicine(request):
    if request.method == 'POST':
        try:
            # Ambil data dari form
            medicine_name = request.POST['medicine_name']
            medicin_type = request.POST['medicin_type']
            medicine_price = request.POST['medicine_price']
            medicine_stock = request.POST['medicine_stock']
            
            # Simpan data ke database
            Medicine.objects.create(
                medicine_name=medicine_name,
                medicin_type=medicin_type,
                medicine_price=medicine_price,
                medicine_stock=medicine_stock
            )

            # Berikan pesan sukses
            messages.success(request, 'Medicine created successfully!')
            return redirect('medicine')

        except:
            # Berikan pesan gagal
            messages.error(request, 'Failed to create medicine.')
            return redirect('create_medicine')
    return render(request, 'medicine/createMedicine.html')

def update_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    if request.method == 'POST':
        try:
            medicine.medicine_name = request.POST['medicine_name']
            medicine.medicin_type = request.POST['medicin_type']
            medicine.medicine_price = request.POST['medicine_price']
            medicine.medicine_stock = request.POST['medicine_stock']
            medicine.save()
            
            messages.success(request, 'Medicine updated successfully!')
            return redirect('medicine')
    
        except Exception as e:
            # Berikan pesan gagal
            messages.error(request, 'Failed to create medicine.')
            return redirect('update_medicine')
    return render(request, 'medicine/updateMedicine.html', {'medicine': medicine})

def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine')  # Setelah hapus, redirect ke halaman list
    return render(request, 'medicine/deleteMedicine.html', {'medicine': medicine})