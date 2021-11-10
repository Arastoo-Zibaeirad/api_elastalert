from django.db import models

# Create your models here.

class Rule(models.Model):
    name = models.CharField(max_length=200, unique=True)
    index_name = models.TextField(blank=True, null=True)
    # sequence = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'

    def __str__(self):
        return self.name

    def create_query(self):
        return f'{self.query.event_category} where {self.query.condition}'
    #     if self.sequence:
    #         return f'sequence\n  [{self.query.event_category} where {self.query.condition}]'    

    #     elif self.sequence == False:
    #         return f'{self.query.event_category} where {self.query.condition}'
    def create_query_sequence(self):
        return f'sequence\n  [{self.query.event_category} where {self.query.condition}]'

class Query(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, related_name='query')
    event_category = models.CharField(max_length=100)
    condition = models.CharField(max_length=200)
    sequence = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        if self.sequence == False:
            return self.rule.create_query()
        elif self.sequence:
            return self.rule.create_query_sequence()


