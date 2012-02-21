
def remove_old_save_new(instance, model_class, *args, **kwargs):
    #remove any old entries
    old_entries = model_class.objects.filter(wkt_hash=instance.wkt_hash)
    for entry in old_entries:
        model_class.delete(entry)
    #save the new entry
    super(model_class, instance).save(*args, **kwargs)