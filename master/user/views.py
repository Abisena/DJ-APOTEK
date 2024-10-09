from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
# Create your views here.

def user(request):
    users = User.objects.all()
    return render(request, 'user.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        try:
            # Ambil data dari form
            username = request.POST['username']
            email = request.POST['email']
            role = request.POST['role']
            
            # Simpan data ke database
            User.objects.create(
                username=username,
                email=email,
                role=role,
            )

            # Berikan pesan sukses
            messages.success(request, 'User created successfully!')
            return redirect('user')

        except:
            # Berikan pesan gagal
            messages.error(request, 'Failed to create User.')
            return redirect('create_user')
    return render(request, 'createUser.html')


def update_user(request, id):
    medicine = get_object_or_404(user, id=id)
    if request.method == 'POST':
        try:
            user.name = request.POST['name']
            user.email = request.POST['email']
            user.role = request.POST['role']
            medicine.save()
            
            messages.success(request, 'Medicine updated successfully!')
            return redirect('user')
    
        except Exception as e:
            messages.error(request, 'Failed to create medicine.')
            return redirect('update_user')
    return render(request, 'updateMedicine.html', {'user': user})

def delete_user(request, id):
    medicine = get_object_or_404(user, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user')
    return render(request, 'deleteMedicine.html', {'user': user})