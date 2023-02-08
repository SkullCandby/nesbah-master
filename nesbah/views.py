from django.shortcuts import redirect


def main(request):
    return redirect('account/index')