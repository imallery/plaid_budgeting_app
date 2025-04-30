import 'package:client/data/respositories/plaid_link_repository.dart';
import 'package:client/widgets/bloc_providers.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class RepositoryProviders extends StatelessWidget
{
  RepositoryProviders({super.key});

  @override
  Widget build( BuildContext context )
  {
    return MultiRepositoryProvider(
        providers:[
          RepositoryProvider(
              lazy: false,
              create: (context) => PlaidLinkRepository()
          )
        ],
        child: BlocProviders()
    );
  }
}