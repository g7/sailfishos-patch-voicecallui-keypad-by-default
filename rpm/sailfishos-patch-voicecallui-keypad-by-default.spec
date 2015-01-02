# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-patch-voicecallui-keypad-by-default

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Keypad open by default in voicecall-ui
Version:    1.1.1.26
Release:    1
Group:      Applications/Productivity
License:    GPLv2+
BuildArch:  noarch
URL:        http://me.medesimo.eu
Source0:    %{name}-%{version}.tar.bz2
Source100:  sailfishos-patch-voicecallui-keypad-by-default.yaml
Requires:   patchmanager
Requires:   sailfish-version >= 1.1.1-10.22.26.jolla.armv7hl

%description
Opens the dialer keypad by default


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager
# >> files
# << files
