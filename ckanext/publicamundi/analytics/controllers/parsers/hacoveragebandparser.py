from ckanext.publicamundi.analytics.controllers.parsedinfo.hacoveragebandsinfo import HACoverageBandsInfo
from ckanext.publicamundi.analytics.controllers.parsers.haparser import HAParser
from ckanext.publicamundi.analytics.controllers.parsers.hausedcoveragesparser import HAUsedCoveragesParser


class HACoverageBandParser(HAParser):
    """
    Specialized HAParser for information about specific bands of a coverage.
    """
    __author__ = "<a href='mailto:merticariu@rasdaman.com'>Vlad Merticariu</a>"

    def __init__(self, log_lines):
        """
        Class constructor.
        :param list[str] log_lines: the lines of the log
        :param <string> coverage_name: the coverage for which the information is parsed.
        """
        HAParser.__init__(self, log_lines)
        self.coverage_names = HAUsedCoveragesParser(log_lines).parse_accessed_coverages()

    def parse_coverage_band_line(self, coverage_name, line):
        """
        Parses a line in the log file which already contains the coverage.
        :param <string> line: a log line in which the searched coverage is addressed.
        :return: <[HACoverageBandInfo]> list of objects describing the bands accessed in the current line.
        """
        ret = []
        if self.range_subset_key in line.lower():
            split = line.split(self.range_subset_key)
            focus = split[1]
            # check if the range subset is given in the middle of the request or at the end
            if self.and_key in focus:
                # in the middle, do further split
                focus = focus.split(self.and_key)[0]
            else:
                # otherwise focus is at the end followed by a space
                focus = focus.split(" ")[0]
            # check if there are several bands accessed
            if self.comma_key in focus:
                bands = focus.split(self.comma_key)
            elif self.column_key in focus:
                bands = focus.split(self.column_key)
            else:
                bands = [focus]
            # add all the bands to the result
            date = HAParser.parse_date(line)
            for band in bands:
                ret.append(HACoverageBandsInfo(date, coverage_name, band, 1))
        return ret

    def assign_colors_to_bands(self, band_info_list):
        """
        Assigns colors from the color_list to a list of HACoverageBandInfo objects.
        :param <[HACoverageBandInfo]> band_info_list: the list of objects to which colors are to be assigned.
        """
        i = 0
        for band_info in band_info_list:
            band_info.color = self.color_list[i % len(self.color_list)]
            i += 1

    def parse(self):
        """
        Parses the current log file and returns information about the bands that have been accessed.
        :return: <[HACoverageBandInfo]> a list of objects describing the bands accessed.
        """
        result = []
        for coverage_name in self.coverage_names:
            band_info_list = []
            for line in self.log_lines:
                validated_line = self.validate_line(line)
                if coverage_name.lower() in validated_line:
                    band_info_list += self.parse_coverage_band_line(coverage_name, validated_line)
            merged_list = self.merge_info_list(band_info_list, HACoverageBandsInfo.band_property_key)
            self.assign_colors_to_bands(merged_list)
            result += merged_list
        return result

    """
    Key definitions, to know what to look for in the log file.
    """
    range_subset_key = "rangesubset="
    and_key = "&"
    comma_key = ","
    column_key = ":"
    color_list = ["#FE2619", "#1CD52B", "#2462D4", "#2462D4", "#9423D2"]
