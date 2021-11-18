from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.

class Rule(models.Model):
    name = models.CharField(max_length=200, unique=True)
    index_name = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


    # @property
    # def total(self):
    #     x=""
    #     queries = self.queries.all()
    #     if queries[0].sequence == False:
    #         z = (f"{queries[0].event_category} where {queries[0].condition}")
    #     elif queries[0].sequence:
    #         for i in range (len(queries)):
    #             b = "sequence\\n "
    #             c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n  ")
    #             x = x + c

    #         z = b + x 
    #         print(z)
    #     return z   

    @property
    def total(self):
        x=""
        queries = self.queries.all()
        # config = self.config.all() ##config.all() nadare
        if self.config.sequence == False:
            z = (f"{queries[0].event_category} where {queries[0].condition}")
        elif self.config.sequence:
            for i in range (len(queries)):
                b = "sequence\\n "
                c = (f"[{queries[i].event_category} where {queries[i].condition}]\\n  ")
                x = x + c

            z = b + x 
            print(z)
        return z   

    @property
    def sequence(self):
        # sequence = self.config.get(sequence=True)
        if self.config.sequence:
            return True
        else:
            return False

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'

    def __str__(self):
        return self.name

    # def create_query(self):
    #     # return f"{self.queries.event_category} where {self.queries.condition}"
    # #     if self.sequence:
    # #         return f'sequence\n  [{self.query.event_category} where {self.query.condition}]'    

    # #     elif self.sequence == False:
    #     return f'{self.queries.event_category} where {self.queries.condition}'
    # def create_query_sequence(self):
    #     return f'sequence\n  [{self.queries.event_category} where {self.queries.condition}]'

class Query(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='queries')
    
    ANY = 'any'
    PROCESS = 'process'
    NETWORK = 'network'
    FILE = 'file'
    REGISTRY = 'registry'
    AUTHENTICATION = 'authentication'
    CONFIGURATION = 'configuration'
    DATABASE = 'database'
    DRIVER = 'driver'
    HOST = 'host'
    IAM = 'iam'
    INTRUSION_DETECTION = 'intrusion_detection'
    MALWARE = 'malware'
    PACKAGE = 'package'
    SESSION = 'session'
    THREAT = 'threat'
    WEB = 'web'

    event_category_fields = (
        (ANY, "any"),
        (PROCESS, "process"),
        (NETWORK, "network"),
        (FILE, "file"),
        (REGISTRY, "registry"),
        (AUTHENTICATION, "authentication"),
        (CONFIGURATION, "configuration"),
        (DATABASE, "database"),
        (DRIVER, "driver"),
        (HOST, "host"),
        (IAM, "iam"),
        (INTRUSION_DETECTION, "intrusion_detection"),
        (MALWARE, "malware"),
        (PACKAGE, "package"),
        (SESSION, "session"),
        (THREAT, "threat"),
        (WEB, "web"),
    )
   
    event_category = models.CharField(max_length=32, default=ANY, choices=event_category_fields)
    condition = models.CharField(max_length=200)
    by = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        return f"{self.rule}"
        # if self.sequence == False:
        #     return f'{self.event_category} where {self.condition}'
        # elif self.sequence:
        #     return f'sequence\n  [{self.event_category} where {self.condition}] '    

       
class Config(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, related_name='config')
    sequence = models.BooleanField(default=False)
    until = models.BooleanField(default=False)
    maxspan = models.BooleanField(default=False)
    size = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.rule}"