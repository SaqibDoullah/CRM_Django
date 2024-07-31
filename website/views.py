from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    """
    This function handles the home page of the application. It displays all records and handles user login.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.

    Returns:
    HttpResponse: If the request method is POST, it authenticates the user, logs them in, and redirects them to the home page.
    If the authentication fails, it displays an error message and redirects them to the home page.
    If the request method is not POST, it renders the 'home.html' template with all records.
    """
    records = Record.objects.all()
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})



def logout_user(request):
    """
    This function handles the user logout process. It logs out the user from the current session,
    displays a success message, and redirects the user to the home page.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.

    Returns:
    HttpResponseRedirect: Redirects the user to the home page after logging them out.
    """
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def register_user(request):
    """
    This function handles the user registration process in a Django web application.
    It checks if the request method is POST, and if so, it processes the registration form.
    If the form is valid, it saves the user to the database, authenticates the user, logs them in,
    displays a success message, and redirects them to the home page.
    If the request method is not POST, it renders the 'register.html' template with an empty registration form.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.

    Returns:
    HttpResponseRedirect: If the user is successfully registered and logged in, it redirects the user to the home page.
    render: If the request method is not POST, or if the form data is not valid, it renders the 'register.html' template
    with the form.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
    """
    This function retrieves and displays a specific customer record based on the provided primary key (pk).
    Only authenticated users are allowed to view the record.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.
    pk (int): The primary key of the customer record to be retrieved.

    Returns:
    HttpResponse: If the user is authenticated, it renders the 'record.html' template with the retrieved record.
    HttpResponseRedirect: If the user is not authenticated, it redirects the user to the home page with a message
    requiring the user to log in.
    """
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')



def delete_record(request, pk):
    """
    Deletes a record from the database based on the provided primary key (pk).
    Only authenticated users are allowed to delete records.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.
    pk (int): The primary key of the record to be deleted.

    Returns:
    HttpResponseRedirect: If the user is authenticated and the record is successfully deleted,
    it redirects the user to the home page with a success message.
    HttpResponseRedirect: If the user is not authenticated, it redirects the user to the home page with a message
    requiring the user to log in.
    """
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')


def add_record(request):
    """
    This function handles the addition of a new record to the database.
    It checks if the user is authenticated before allowing the record to be added.
    If the user is authenticated and the request method is POST, it validates the form data.
    If the form data is valid, it saves the record to the database, displays a success message,
    and redirects the user to the home page.
    If the user is not authenticated, it displays a message requiring the user to log in.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.

    Returns:
    HttpResponseRedirect: If the user is authenticated and the record is successfully added,
    it redirects the user to the home page.
    render: If the user is authenticated but the request method is not POST, or if the form data is not valid,
    it renders the 'add_record.html' template with the form.
    HttpResponseRedirect: If the user is not authenticated, it redirects the user to the home page with a message
    requiring the user to log in.
    """
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def update_record(request, pk):
    """
    This function handles the updating of an existing record in the database.
    It checks if the user is authenticated before allowing the record to be updated.
    If the user is authenticated and the request method is POST, it validates the form data.
    If the form data is valid, it updates the record in the database, displays a success message,
    and redirects the user to the home page.
    If the user is not authenticated, it displays a message requiring the user to log in.

    Parameters:
    request (HttpRequest): The request object containing information about the user and the request.
    pk (int): The primary key of the record to be updated.

    Returns:
    HttpResponseRedirect: If the user is authenticated and the record is successfully updated,
    it redirects the user to the home page.
    render: If the user is authenticated but the request method is not POST, or if the form data is not valid,
    it renders the 'update_record.html' template with the form.
    HttpResponseRedirect: If the user is not authenticated, it redirects the user to the home page with a message
    requiring the user to log in.
    """
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')