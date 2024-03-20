import React from 'react';

import { DashboardCore } from '@splunk/dashboard-core';
import { DashboardContextProvider } from '@splunk/dashboard-context';
import EnterpriseViewOnlyPreset from '@splunk/dashboard-presets/EnterpriseViewOnlyPreset';
import SplunkThemeProvider from '@splunk/themes/SplunkThemeProvider';
import definition from './definition.json';

const themeToVariant = {
    enterprise: { colorScheme: 'light', family: 'enterprise' },
    enterpriseDark: { colorScheme: 'dark', family: 'enterprise' },
    prisma: { colorScheme: 'dark', family: 'prisma' },
};

// use DashboardCore to render a simple dashboard
// NOTICE: If you are on Dashboard Core versions LOWER than 25.X.X, preset will be a prop for <DashboardCore> instead of 
// <DashboardContextProvider>

const DashboardExample = () => {
    return (
        <SplunkThemeProvider {...themeToVariant.prisma}>
            <DashboardContextProvider 
                preset={EnterpriseViewOnlyPreset}
                initialDefinition={definition}
            >
                <DashboardCore
                    width="100%"
                    height="100%"
                />
            </DashboardContextProvider>
        </SplunkThemeProvider>
    );
};

export default DashboardExample;