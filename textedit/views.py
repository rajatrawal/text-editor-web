from typing import Text
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    dj_text = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "off")
    capitalizeAll = request.POST.get("capitalizeAll", "off")
    newLineRemoval = request.POST.get("newLineRemoval", "off")
    characterCount = request.POST.get("characterCount", "off")
    print("characterCount : "+characterCount)
    spaceRemover = request.POST.get("spaceRemover", "off")
    analyze_text = dj_text
    text = analyze_text
    params = {"analyze_text": analyze_text}
    punc_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
    if(removepunc == "on"):
        analyze_text = ""
        for i in text:
            if i not in punc_list:
                analyze_text += i
                text = analyze_text
            else:
                pass
        params = {"analyze_text": analyze_text}
    if(capitalizeAll == "on"):
        analyze_text = ""
        for i in text:
            analyze_text += i.upper()
            text = analyze_text
        params = {"analyze_text": analyze_text}
    if(newLineRemoval == "on"):
        analyze_text = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyze_text = analyze_text + char
            else:
                analyze_text += " "
        text = analyze_text
        params = {'analyze_text': analyze_text}
    if(spaceRemover == "on"):
        analyze_text = ""
        for i, char in enumerate(text):
            if i+1 < len(text):
                if not(text[i] == " " and text[i+1] == " "):
                    analyze_text += char
            else:
                analyze_text += char

        text = analyze_text
        params = {"analyze_text": analyze_text}
    if characterCount == "on":
        params = {"analyze_text": analyze_text,
                  "character_count": len(analyze_text)}
    return render(request, "analyze.html", params)
