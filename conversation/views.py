from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm


# view for handling conversations
# NOTE: primary key here is for finding item
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    # if the item is created by yourself then you can't have conversation
    if item.created_by == request.user:
        return redirect("dashboard:index")
    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user.id]
    )

    # send directly to conversation page if they already had a conversation
    if conversations:
        return redirect("conversation:detail", pk=conversations.first().id)

    # if the conversation is first one
    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            # creating a new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            # creating conversation message
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("item:detail", pk=item_pk)
    else:
        form = ConversationMessageForm()
    return render(request, "conversation/new.html", {"form": form})


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, "conversation/inbox.html", {"conversations": conversations})


@login_required
def detail(request, pk):  # this pk is primary key of our conversation
    # conversations = get_object_or_404(Conversation,pk=pk)
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect("conversation:detail", pk=pk)
    else:
        form = ConversationMessageForm()
    return render(
        request,
        "conversation/detail.html",
        {"conversation": conversation, "form": form},
    )
