from datetime import datetime, timedelta
from webapp.models import Task, Type, Project
from django.db.models import Q

first task

end_date = datetime.now() - timedelta(days = 30)
start_date = datetime.now()

q_1 = Q(status__name='done')
q_2 = Q(created_at__range=(start_date, end_date))

Task.objects.filter(q_1&q_2)

second task

Type.objects.filter(tasks__project__name='project2')

third task

Project.objects.filter(tasks__description__icontains='test')

