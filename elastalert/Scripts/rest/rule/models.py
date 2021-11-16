from django.db import models

# Create your models here.

class Rule(models.Model):
    name = models.CharField(max_length=200, unique=True)
    index_name = models.TextField(blank=True, null=True)
    # sequence = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


    @property
    def total(self):
        a=""
        queries = self.queries.all()
        for query in queries:
            # for i in range(len(queries)):
            if query.sequence == False:
                a += str(f"{query.event_category} where {query.condition}")
            elif query.sequence:
                a += str(f"sequence\\n [{query.event_category} where {query.condition}] ")

            # a+=str(query.event_category)
        return a    

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
    sequence = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Query'
        verbose_name_plural = 'Queries'

    def __str__(self):
        if self.sequence == False:
            return f'{self.event_category} where {self.condition}'
        elif self.sequence:
            return f'sequence\n  [{self.event_category} where {self.condition}] '    

       
