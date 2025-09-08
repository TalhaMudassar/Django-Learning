class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'roll')

admin.site.register(profile, ProfileAdmin)
