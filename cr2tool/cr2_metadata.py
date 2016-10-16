import exifread


class Cr2Metadata:
    def __init__(self, filename):
        f = open(filename, 'rb')
        self.tags = exifread.process_file(f)

    def exposure_bias(self):
        exposure_bias_tags = self.tags['EXIF ExposureBiasValue']
        if not exposure_bias_tags:
            raise IOError('No exposure bias tag')
        if len(exposure_bias_tags.values) > 1:
            raise IOError('Multiple exposure bias values are not supported')
        ratio = self.tags['EXIF ExposureBiasValue'].values[0]
        return ratio.num / ratio.den
