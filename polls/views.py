# polls/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # Add this import
from .models import Poll, Choice

@login_required
def poll_list(request):
    polls = Poll.objects.all()
    # print(polls)
    return render(request, 'polls/poll_list.html', {'polls': polls})

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    print(request)
    print(poll.choice_set)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form with an error message.
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'error_message': "Please select a valid choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('poll_detail', poll_id=poll_id)
    

@login_required
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})
