# .service

This is config for `systemctl` service. If you have more modems, create .service for each gammu-smsd config file.

Systemctl services files stores in `/etc/systemd/system`

Change `User` to you system username. If you hame more modems, don't forget to change `-c /etc/gammu-smsdrc` in `ExecStart` to your second gammu config.

## Configuration

```bash
[Unit]
Description=Modem 1 Receiver (Gammu)          # Description for service
serviceAfter=network.target                   # Start after network service
StartLimitIntervalSec=0                       # Limit interval for start service

[Service]
Type=simple                                   # Type of service
Restart=always                                # Always restart if service goes down
RestartSec=1                                  # Seconds to restart after service down
User=user                                     # System username
ExecStart=gammu-smsd -c /etc/gammu-smsdrc     # Start gammu-smsd with modem config

[Install]
WantedBy=multi-user.target
```

## Monitoring

1. Check services running
```
systemctl status gammu-modem-1.service
```
2. Restart services
```
systemctl restart gammu-modem-1.service
```
3. Start service
```
systemctl start gammu-modem-1.service
```
4. Stop service
```
systemctl stop gammu-modem-1.service
```

If you have more modems, you need to launch each service for each modem.
