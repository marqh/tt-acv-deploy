Name:		registry-core-tt-acv
Version:	0.1
Release:	1
Summary:	TT ACV linked data registry

License:	apache
URL:		https://github.com/wmo-registers/tt-acv-deploy

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tar.gz

Requires:       java-1.7.0-openjdk
Requires:       nginx
Requires:       tomcat7


%description


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
install -D etc/sudoers.d/uklSudoers.conf $RPM_BUILD_ROOT/etc/sudoers.d/uklSudoers.conf
mkdir -p $RPM_BUILD_ROOT/opt/ldregistry/ui
mkdir -p $RPM_BUILD_ROOT/var/opt/ldregistry
mkdir -p $RPM_BUILD_ROOT/var/log/ldregistry
install -D var/lib/tomcat7/webapps/ROOT.war $RPM_BUILD_ROOT/var/lib/tomcat7/webapps/ROOT.war

%pre
SERVICE='tomcat'#7
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    service tomcat7 stop
fi
alternatives --set java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java


%post
service tomcat7 start

%preun
SERVICE='tomcat'#7
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    service tomcat7 stop
fi

%postun
rm -rf /opt/ldregistry
rm -rf /var/lib/tomcat7/webapps/ROOT

%clean
rm -rf $RPM_BUILD_ROOT



%files
/etc/sudoers.d/uklSudoers.conf
%defattr(775,root,tomcat,775)
/var/lib/tomcat7/webapps/ROOT.war
%dir /opt/ldregistry
%dir /opt/ldregistry/ui
%dir /var/opt/ldregistry
%dir /var/log/ldregistry


%changelog
* Fri Mar 27 2015 markh <markh@metarelate.net> - 0.1-1
- Initial version
