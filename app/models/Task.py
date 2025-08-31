from datetime import datetime
from app.extensions import db


class Task(db.Model):
    __tablename__ = 'tasks'

    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def add_task(cls, task):
        new_task = cls(task=task)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @classmethod
    def get_all_tasks(cls):
        return cls.query.all()

    @classmethod
    def get_task_by_id(cls, task_id):
        return cls.query.get(task_id)

    @classmethod
    def update_task(cls, task_id, task_data):
        task = cls.query.get(task_id)
        if task:
            task.task = task_data.get("task", task.task)
            task.completed = task_data.get("completed", task.completed)
            db.session.commit()
            return task
        return None

    @classmethod
    def delete_task(cls, task_id):
        task = cls.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {"message": "Task deleted successfully"}
        return None
