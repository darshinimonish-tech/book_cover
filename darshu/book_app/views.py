from django.shortcuts import render

# View function to display the book cover page
def book_cover(request):
    return render(request, 'book.html')
