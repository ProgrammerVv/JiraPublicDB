import dbrequests
import clickhouse_driver


class Issues(models.Model):  # Model for course
    issue_id = models.CharField("id issue", max_length=100)
    issue_key = models.CharField("Issue Key")
    project_name = models.IntegerField("Project Name")
    issue_type = models.FloatField("Issue Type")

    # def __str__(self):
    #     return self.course_title

