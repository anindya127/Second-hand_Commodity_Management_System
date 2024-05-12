from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item

from .forms import MessageForm
from .models import Conversation, Message

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect("dashboard:index")
    
    conversation = Conversation.objects.filter(item=item, member__in=[request.user.id])

    # if conversation():
    #     pass

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.member.add(request.user)
            conversation.member.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.user = request.user
            conversation_message.save()

            return redirect("item:detail", pk=item.pk)
    else:
        form = MessageForm()

    return render(request, "conversation/new.html", {
        "form": form, 
        "item": item,
        })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(member__in=[request.user.id])

    return render(request, "conversation/inbox.html", {
        "conversations": conversations,
        })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(member__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.user = request.user
            conversation_message.save()

            conversation.save()

            return redirect("conversation:detail", pk=pk)
    else:
        form = MessageForm()

    return render(request, "conversation/detail.html", {
        "conversation": conversation,
        "form": form,
        })