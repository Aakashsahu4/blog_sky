from django.db import models
from master import utils as master_utils
from account import models as account_models



class Blog(master_utils.CreatedModifiedModel):

	user_profile = models.ForeignKey(account_models.User,on_delete=models.CASCADE)
	title = models.CharField(max_length=45)
	content = models.TextField()
	image = models.ImageField(upload_to='blog/images',null=True,blank=True)


	def __str__(self):
		return self.title


class Notification(master_utils.CreatedModifiedModel):

    from_user = models.ForeignKey(
        account_models.User,
        null=True,
		related_name='noti_from',
        on_delete=models.CASCADE,
    )
    to_user = models.ForeignKey(
        account_models.User,
        null=True,
		related_name='noti_to',
        on_delete=models.CASCADE,
    )
    blog = models.ForeignKey(
        Blog,
        null=True,
        related_name="blog_notification",
        blank=True,
        on_delete=models.CASCADE,
    )
    notification_text = models.CharField(max_length=200, null=True, blank=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification__{self.id}'