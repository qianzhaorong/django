from django.test import TestCase
from django.test import Client

from .models import Student

# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='qzr',
            sex=1,
            email='11@qq.com',
            profession='程序员',
            qq='2222',
            phone='1111',
        )
    
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='qq',
            sex=1,
            email='11@qq.com',
            profession='程序员',
            qq='3333',
            phone='1111',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容和展示不一致')

    def test_filter(self):
        Student.objects.create(
            name='qq',
            sex=1,
            email='11@qq.com',
            profession='程序员',
            qq='3333',
            phone='1111',
        )
        name = 'qzr'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的纪录'.format(name))

    def test_get_index(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_client',
            sex=1,
            email='222@qq.com',
            profession='程序员',
            qq='2222',
            phone='222',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_clien' in response.content, 'response content must contain `test_for_post`')
    
