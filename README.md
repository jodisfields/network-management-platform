# Project Requirements

- [ ] Connect via SSH to all network devices currently in production.
- [ ] Determine the hostname of each device.
- [ ] Determine the model of each device.
- [ ] Determine the serial number of each device.
- [ ] Determine the uptime from each the devices.
- [ ] Determine the version of each device.
- [ ] Identify the device type to determine the correct commmands to execute.
- [ ] Obtain a list of CDP neighbours from each the devices.
- [ ] Obtain a list of interface descriptions from each the devices.
- [ ] Obtain a list of interfaces from each the devices.
- [ ] Obtain a list of LDDP Neighbours from each the devices.
- [ ] Obtain a list of OSPF NNeighbours from each the devices.
- [ ] Obtain a list of VLANs from each the devices.
- [ ] Obtain the number of active SFPs for each device.
- [ ] Obtain the running configuration from each the devices.
- [ ] Obtain the total number of SFPs for each device.


# Testing API Funtionality

#### Users

```shell
curl -H 'Accept: application/json; indent=4' -u USERNAME:PASSWORD http://127.0.0.1:8000/users/
```

#### Groups

```shell
curl -H 'Accept: application/json; indent=4' -u USERNAME:PASSWORD http://127.0.0.1:8000/groups/
```

# Creating Models

```python
from django.db import models


class Example(models.Model):
    class Meta:
        db_table = "Example"
        verbose_name = "Example"
        verbose_name_plural = "Example"

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default=None,
        verbose_name="Title",
        help_text="Title.",
    )

    category = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default="",
        verbose_name="Category",
        help_text="Category.",
    )


    def __str__(self):
        return self.Example
```


