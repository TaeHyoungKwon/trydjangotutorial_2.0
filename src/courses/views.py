from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course


class CourseCreateView(View):
    template_name = "courses/course_create.html"

    def get(self, request, *args, **kwargs):
        #GET
        form = CourseModelForm()
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        #POST
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}

        return render(request, self.template_name, context)


class CourseDeleteView(View):
    template_name = "courses/course_delete.html"

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)

        return obj
    
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('../../')

        return render(request, self.template_name, context)

    
class CourseView(View):
    template_name = "courses/course_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}

        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj

        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        print(self.queryset)
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        print(context)
        return render(request, self.template_name, context)


class CourseUpdateView(View):
    template_name = "courses/course_update.html"

    def get_object(self):
        '''
        url로 넘어오는 id 값을 return 한다.
        '''
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        '''
        화면을 보여주기 위한 메소드이다.
        obj가 있을 시에는 기존의 obj를 form 값에 미리 넣어주고(여기서 context도 setting을 해줍니다.),
        그렇지 않을 시에는 빈 context를 리턴한다.
        '''
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form

        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            print(form)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)
