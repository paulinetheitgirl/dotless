#!/usr/bin/python
#
# Copyright 2008, Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This code sample retrieves API usage information as it is shown in the
AdWords API Center that belongs to the customer issuing the request."""

import datetime
import SOAPpy


# Provide AdWords login information.
email = 'INSERT_LOGIN_EMAIL_HERE'
password = 'INSERT_PASSWORD_HERE'
client_email = 'INSERT_CLIENT_LOGIN_EMAIL_HERE'
useragent = 'INSERT_COMPANY_NAME: AdWords API Python Sample Code'
developer_token = 'INSERT_DEVELOPER_TOKEN_HERE'
application_token = 'INSERT_APPLICATION_TOKEN_HERE'

# Define SOAP headers.
headers = SOAPpy.Types.headerType()
headers.email = email
headers.password = password
headers.clientEmail = client_email
headers.useragent = useragent
headers.developerToken = developer_token
headers.applicationToken = application_token

# Set up service connection. To view XML request/response, change value of
# info_service.config.debug to 1. To send requests to production
# environment, replace "sandbox.google.com" with "adwords.google.com".
namespace = 'https://sandbox.google.com/api/adwords/v12'
info_service = SOAPpy.SOAPProxy(namespace + '/InfoService',
                                header=headers)
info_service.config.debug = 0

# Get quota usage.
total_limit = info_service.getUsageQuotaThisMonth()
free_quota_limit = info_service.getFreeUsageQuotaThisMonth()
start_date = datetime.datetime.now().strftime('%Y-%m-01T00:00:00')
end_date = datetime.datetime.now().strftime('%Y-%m-%dT00:00:00')
total_used = info_service.getUnitCount(SOAPpy.Types.untypedType(start_date),
                                       SOAPpy.Types.untypedType(end_date))
if long(total_used) > long(free_quota_limit):
  free_quota_used = free_quota_limit
else:
  free_quota_used = total_used

# Display quota usage info.
print 'Free API units used is "%s".' % (free_quota_used)
print 'Total API units used is "%s".' % (total_used)
print 'Free API units remaining is "%s".' % \
    (long(free_quota_limit) - long(free_quota_used))
print 'System-defined quota cap is "%s".' % (total_limit)
