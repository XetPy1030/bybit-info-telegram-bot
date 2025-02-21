from tortoise import models, fields


class BalanceItem(models.Model):
    balance = fields.ForeignKeyField("models.Balance", related_name="items")

    account_type = fields.CharField(max_length=255)
    origin_balance = fields.FloatField()
    quote_balance = fields.FloatField()

    created_at = fields.DatetimeField(auto_now_add=True)


class Balance(models.Model):
    quote_coin = fields.CharField(max_length=255)
    origin_total_balance = fields.FloatField()
    quote_total_balance = fields.FloatField()

    items: fields.ManyToManyRelation[BalanceItem]

    created_at = fields.DatetimeField(auto_now_add=True)


class BybitSecretKey(models.Model):
    secret_key = fields.CharField(max_length=511)
    expires_at = fields.DatetimeField(null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
