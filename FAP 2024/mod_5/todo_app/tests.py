import unittest
from app import app, db
from app.models import Task
from datetime import datetime, timezone
from sqlalchemy.exc import InvalidRequestError

class Task(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        """Configura o ambiente de teste."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Usar banco de dados em memória para testes
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Limpa o ambiente de teste."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        """Testa a página inicial."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gerenciador de Tarefas', response.data)

    def test_create_task(self):
        """Testa a criação de uma nova tarefa."""
        response = self.client.post('/create', data=dict(
            title='Teste de Tarefa',
            description='Descrição de teste'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teste de Tarefa', response.data)

    def test_update_task(self):
        """Testa a atualização de uma tarefa existente."""
        # Cria uma tarefa original
        task = Task(title='Tarefa Original', description='Descrição original')
        db.session.add(task)
        db.session.commit()
        task_id = task.id

        # Atualiza a tarefa
        response = self.client.post(f'/update/{task_id}', data=dict(
            title='Tarefa Atualizada',
            description='Descrição atualizada',
            completed='on'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tarefa Atualizada', response.data)

    def test_delete_task(self):
        """Testa a deleção de uma tarefa existente."""
        # Cria uma tarefa para deletar
        task = Task(title='Tarefa para Deletar', description='Será deletada')
        db.session.add(task)
        db.session.commit()
        task_id = task.id

        # Deleta a tarefa
        response = self.client.get(f'/delete/{task_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Tarefa para Deletar', response.data)

    def test_repr(self):
        """Testa a representação string de uma tarefa."""
        task = Task(title='Teste __repr__', description='Descrição para __repr__')
        db.session.add(task)
        db.session.commit()
        expected_repr = f'<Task {task.id}: {task.title}>'
        self.assertEqual(repr(task), expected_repr)

if __name__ == '__main__':
    unittest.main()