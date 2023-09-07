class CommandResult:
    TimeoutError = 'TimeoutError'
    InvalidArguments = 'InvalidArguments'
    Ok = 'Ok'
    Unimplemented = 'Unimplemented'

    def __init__(self, variant, value = None):
        self.variant = variant
        self.value = value

    @staticmethod
    def Speed(value: float):
        return CommandResult('Speed', value)